# Plant Identifier

Identify a plant from a photo using the [PlantNet](https://my.plantnet.org/) API.

This is a small local script, not a web app. Point it at an image, send the leaf to PlantNet, and print the JSON result.

## Setup

```bash
git clone https://github.com/Irsalistic/plants_identifier.git
cd plants_identifier
pip install -r requirements.txt
```

Create a `.env` file in this folder:

```env
plants_api=YOUR_PLANTNET_API_KEY
```

Get a key from [my.plantnet.org](https://my.plantnet.org/).

## Run

By default the script identifies `mango.jpg` as a leaf:

```bash
python plant_identify.py
```

To identify a different photo, change `image_path_1` and `data['organs']` in `plant_identify.py`. Organ values PlantNet accepts include `leaf`, `flower`, `fruit`, and `bark`.

## Layout

```
plant_identify.py     # PlantNet request
testing_packages.py   # leftover helper that lists installed packages
*.jpg / *.jpeg        # sample photos
```

Your API key stays in `.env` and should never be committed.
