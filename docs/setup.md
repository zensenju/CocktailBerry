# Setting up CocktailBerry

CocktailBerry will work after installing all requirements, but you can make your own adjustments.

## Adding new Recipes or Ingredients

There are only limited ingredients and recipes. But you can add your own data to the program as well.
This app uses a sqlite3 Database coupled to the UI. So, it's quite easy to implement new ingredients or even recipes.
Just use the implemented UI for the procedure under the according tabs (**Ingredients** or **Recipes**).

All entered values are checked for reason and if something is wrong, an error message will inform the user what is wrong with the data input. If you want to browse through the databse, I recommend some program like [DB Browser for sqlite](https://sqlitebrowser.org/).

## Setting up the Machine / Modifying other Values

These values are stored under the `custom_config.yaml` file. This file will be created at the first machine run and inherit all default values. Depending on your pumps and connection to the Pi, these can differ from mine and can be changed. If any of the values got a wrong data type, a ConfigError will be thrown with the message which one is wrong. You can also manage your config within CocktailBerry since __version 1.8.0__. Just go to the bottles tab, enter the default (1234) password into the lineedit and click the gear icon. You can then use the UI to change the configuration.

| Value Name              |    Type     | Description                                                                          | Optional |
| :---------------------- | :---------: | :----------------------------------------------------------------------------------- | :------: |
| `UI_DEVENVIRONMENT`     |   _bool_    | Boolean flag to enable some development features                                     |    ❌     |
| `UI_PARTYMODE`          |   _bool_    | En- or disables the recipe tab (to prevent user interaction)                         |    ❌     |
| `UI_MASTERPASSWORD`     |    _str_    | String for password, Use numbers for numpad like '1234'                              |    ❌     |
| `UI_LANGUAGE`           |    _str_    | 2 char code for the language, see [supported languages](languages.md)                |    ❌     |
| `UI_WIDTH`              |    _int_    | Desired interface width, default is 800                                              |    ❌     |
| `UI_HEIGHT`             |    _int_    | Desired interface height, default is 480                                             |    ❌     |
| `PUMP_PINS`             | _list[int]_ | List of the [Pins](#configuring-the-pins-or-used-board) where each Pump is connected |    ❌     |
| `PUMP_VOLUMEFLOW`       | _list[int]_ | List of the according volume flow for each pump in ml/s                              |    ❌     |
| `MAKER_BOARD`           |    _str_    | Used [board](#configuring-the-pins-or-used-board) for Hardware                       |    ❌     |
| `MAKER_NAME`            |    _str_    | Give your Cocktailberry a own name, max 30 chars                                     |    ❌     |
| `MAKER_NUMBER_BOTTLES`  |    _int_    | Number of displayed bottles, can use up to 16 bottles                                |    ❌     |
| `MAKER_SEARCH_UPDATES`  |   _bool_    | Boolean flag to search for updates at program start                                  |    ❌     |
| `MAKER_THEME`           |    _str_    | Choose which [theme](#themes) to use                                                 |    ❌     |
| `MAKER_CLEAN_TIME`      |    _int_    | Time the machine will execute the cleaning program                                   |    ❌     |
| `MAKER_SLEEP_TIME`      |   _float_   | Interval between each UI refresh while generating a cocktail                         |    ❌     |
| `MICROSERVICE_ACTIVE`   |   _bool_    | Boolean flag to post to microservice set up by docker                                |    ✔️     |
| `MICROSERVICE_BASE_URL` |    _str_    | Base URL for microservice (default: http://127.0.0.1:5000)                           |    ✔️     |
| `TEAMS_ACTIVE`          |   _bool_    | Boolean flag to use teams feature                                                    |    ✔️     |
| `TEAM_BUTTON_NAMES`     | _list[str]_ | List of format ["Team1", "Team2"]                                                    |    ✔️     |
| `TEAM_API_URL`          |    _str_    | Endpoint of teams API, default used port by API is 8080                              |    ✔️     |

Depending on your preferred use, these values can differ. Then just run:

```bash
python runme.py
```

Setting up the machine is quite easy as well. Just go to the `Bottles` Tab and select via the dropdown boxes your assigned ingredients. In addition, you can define ingredients which are also there, but are not connected to the machine (under _Ingredients > available_). You can define ingredients in recipes (at _add self by hand_) which should be later added via hand, for example sticky ingredients which would not be optimal for your pump, or only very rarely used in cocktails.

The program will then evaluate which recipe meets all requirements to only show the recipes where even the ingredients added via hand later are available, and the recipe will be shown in the `Maker` Tab.

## Configuring the Pins or used Board

To set up your Board, you can choose between different platforms. The according contolling library for Python needs to be installed. If it's not shipped within the default OS of your board, this will be mentioned here. Currently supported options (boards) are:

- **RPI (Raspberry Pi)**: Using GPIO according to [GPIO-Numbers](https://de.pinout.xyz/) for Pins.

## Themes

Currently, there are following themes:

- **default**: The look and feel of the project pictures. Blue, Orange and Black as main colors.
- **bavaria**: The somewhat light mode of the app. Blue, Black and White as main colors.

## Calibration of the Pumps

You can use the provided calibration program to run a simple overlay for pump adjustment. To start the calibration program you simply add the `--calibration` or `-c` flag to the python run command:

```bash
python runme.py --calibration 
# or just 
python runme.py -c
```

This will start the calibration overlay. You can use water and a weight scale for the process. Use different volumes (for example 10, 20, 50, 100 ml) and compare the weight with the output from the pumps. In the end, you can adjust each pump volume flow by the factor:

$$ \dot{V}_{new} = \dot{V}_{old} \cdot \dfrac{V_{expectation}}{V_{output}} $$

## Cleaning the Machine

CocktailBerry has a build in cleaning function for cleaning at the end of a party. You will find the feature at the option gear under the `Bottles` tab. To start the cleaning process, the master password is needed to prevent unwanted cleaning attempts. CocktailBerry will then go to cleaning mode for the defined time within the config (default is 20 seconds). A message prompt will inform the user to provide enough water for the cleaning process. I usually use a big bowl of warm water to cycle the pumps through one time before changing to fresh water and then running twice times again the cleaning program to fully clean all pumps from remaining fluid.

## Possible Ingredient Choice

If you are unsure, which ingredients you may need or want to connect to CocktailBerry, here is a quick suggestion. You don't need to use all ten slot, but the more you use, the more recipes will be possible:

- Vodka
- White Rum
- Brown Rum
- Orange Juice
- Passion Fruit Juice
- Pineapple Juice
- *optional* Gin
- *optional* Malibu
- *optional* Tequila
- *optional* Grapefruit Juice

In addition, there are some ingredients I would recommend not adding via CocktailBerry but by hand, the most important additional ingredients will be:

- Soft Drinks (Cola, Fanta, Sprite)
- Grenadine Syrup
- Blue Curaçao
- Lemon Juice (just a little, you can also use fresh lemons)
- *optional* Cointreau (you may just not add it if not desired)

With this as your base set up, even if not using the optional ingredients, your CocktailBerry will be able to do plenty of different cocktails.

## Updates

With __version 1.5.0__, there is the option to enable the automatic search for updates at program start. The `MAKER_SEARCH_UPDATES` config can enable this feature. CocktailBerry will then check the GitHub repository for new releases and informs the user about it. If accepted, CocktailBerry will pull the latest version and restart the program afterwards. The migrator will also do any necessary steps to adjust local files, like the database to the latest release.