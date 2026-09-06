"""Identify a plant photo with the PlantNet API."""

import argparse
import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

DEFAULT_IMAGE = "mango.jpg"


def identify(image_path: str, organ: str = "leaf", project: str = "all") -> dict:
    api_key = os.getenv("plants_api")
    if not api_key:
        raise SystemExit(
            "Missing plants_api. Put your PlantNet key in a .env file:\n"
            "  plants_api=YOUR_KEY"
        )
    if not os.path.isfile(image_path):
        raise SystemExit(f"Image not found: {image_path}")

    url = f"https://my-api.plantnet.org/v2/identify/{project}?api-key={api_key}"
    with open(image_path, "rb") as image_file:
        response = requests.post(
            url,
            files=[("images", (os.path.basename(image_path), image_file))],
            data={"organs": [organ]},
            timeout=60,
        )
    try:
        body = response.json()
    except ValueError:
        body = {"raw": response.text}
    return {"status_code": response.status_code, "result": body}


def main() -> None:
    parser = argparse.ArgumentParser(description="Identify a plant from a photo.")
    parser.add_argument("image", nargs="?", default=DEFAULT_IMAGE, help="Path to a plant photo")
    parser.add_argument("--organ", default="leaf", help="Plant organ: leaf, flower, fruit, bark")
    parser.add_argument("--project", default="all", help="PlantNet flora project")
    args = parser.parse_args()

    payload = identify(args.image, organ=args.organ, project=args.project)
    print(payload["status_code"])
    print(json.dumps(payload["result"], indent=2))
    if payload["status_code"] >= 400:
        sys.exit(1)


if __name__ == "__main__":
    main()
