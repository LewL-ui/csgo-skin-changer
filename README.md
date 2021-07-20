## Installation
The skin changer requires [python 3.6](https://www.python.org/downloads/release/python-360/) or greater.

1. Install the required dependencies

    ```
    pip install -U -r requirements.txt
    ```
2. Configure your (`config.json`) file to your liking.

3. Launch CS:GO.

4. Launch the (`skin.py`) file by either using:

    ```
    python skin.py
    ```
    or
    ```
    py skin.py
    ```

## Setup your config
Example weapon config:
```
    "deagle": {
        "id": 1,
        "skinID": 0,
        "float": 0.001
    }
```
If you want to make the weapon StatTrak: 
```
    "deagle": {
        "id": 1,
        "skinID": 0,
        "float": 0.001,
        "statTrak": 9999
    }
```
To change the skin, you change the value of `skinID`, example:
```
    "deagle": {
        "id": 1,
        "skinID": 962,
        "float": 0.001
    }
```
If you want to change the weapons name:
```
    "deagle": {
        "id": 1,
        "skinID": 0,
        "float": 0.001,
        "name": "i cant use this pistol"
    }
```

To keep your actual skin applied on the weapon, set `skinID` to `0`.

You can find skin ids from [here](https://csgostash.com/), finding a skin, and the Finish Catalog is your skin id as seen below:

![alt text](https://github.com/donato-fiore/csgo-skin-swapper/blob/main/skinid.png?raw=true)

## Known Issues
  * The skin swapper has some flaws and crashes some times. Usually a restart of the script fixes it.

