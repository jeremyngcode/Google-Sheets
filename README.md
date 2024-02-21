Google Sheets
=============

Intro
-----
After using Excel for so long, I decided to give a web-based solution like Google Sheets a try. I remember classes being one of the harder concepts to learn when I first picked up Python, so I took this chance also to practise it.

The idea is that for each Google spreadsheet, I would initalize a `Sheet` class object from sheet.py with something like this:
```py
sheet1 = Sheet(
    GOOGLE_CREDS_PATH, SPREADSHEET_ID, *sheet_tabs
)
```
Through `sheet1`, I can then execute basic functions like fetching and writing values onto my spreadsheet, all while minimizing and abstracting away a lot of code clutter.

Getting Started
---------------
1. We first need to create a Google Service Account and obtain credentials in the form of a JSON file download. Instructions for this process can be found [here](https://developers.google.com/workspace/guides/create-credentials#service-account).

2. Enable the Google Sheets API at [Google Cloud Console](https://console.cloud.google.com/apis).

3. Head to our Google spreadsheet(s) and grant our new bot (service account) the 'Editor' access.

4. Configure [settings.py](settings.py)
	- **Spreadsheets**
		- Fill in `SPREADSHEET_ID` with our Google spreadsheet id. This id is a string of characters that can be found at the end of our spreadsheet url link.
		- Fill in `sheet_tabs` with the titles of our spreadsheet tabs.
		- For more spreadsheets, simply repeat the code with different variable names like this:
		  ```py
		  SPREADSHEET_ID_2 = 'sexy-monkey-xyz-789'
		  sheet_tabs_2 = ('tab title 1', 'tab title 2')
		  ```
	- **Creds / Secret keys**
		- Fill in `GOOGLE_CREDS_PATH` with the path to the JSON file we just downloaded.
		- Put in any relevant API / Secret keys here (more on this later). I have also provided a .env template file to use with `load_dotenv()`.

5. Set up [Update_Google_Sheets.py](Update_Google_Sheets.py) (main script file)
	- Fill in required functions (more on this later).
	- Initialize all spreadsheets we entered in settings.py by placing the following code on top:
	  ```py
	  sheet1 = Sheet(GOOGLE_CREDS_PATH, SPREADSHEET_ID, *sheet_tabs)
	  sheet2 = Sheet(GOOGLE_CREDS_PATH, SPREADSHEET_ID_2, *sheet_tabs_2)
	  # sheet3 = ...
	  # sheet4 = ...
	  # ...
	  ```

6. Begin writing our code!

Methods ([sheet.py](sheet.py))
------------------------------
While it's possible I add more `Sheet` methods based on my needs along the way, they are pretty basic as of now. Usage is also rather straightforward, although I did have a little trouble initially with the way you needed to format the list brackets when writing values.

Example usage for retrieving values in the 2nd sheet tab and in column A:
```py
values = sheet1.get_values(
    sheet_tab=sheet1.tabs[1],
    cells_range='A:A'
)
```
Example usage for writing values in the 3rd sheet tab on cells B2 to B4:
```py
values_to_write = [['value1'], ['value2'], ['value3']]
sheet1.update_values(
    sheet_tab=sheet1.tabs[2],
    cells_range='B2:B4',
    values=values_to_write
)
```

That being said, I do think that the `update_list_values()` method is worthy of mention.

This method calls `get_values()`, applies a specified function on those values, and then also writes the resulting output values with `update_values()`. This is why in Getting Started, we added external functions to import, along with any associated keys those functions might require. I coded this method with one of my mini utility packages ([jersutils](https://github.com/jeremyngcode/jersutils)) in mind, so it is supposed to work specifically with some of the functions in it.

The tl;dr is that if you have a column of say a list of Ethereum addresses on your spreadsheet and you wanted to write their ETH balances on the same row but on a different column (probably an adjacent column), you can do that with just one line of code.

Example usage if Ethereum address list is on column B of the 1st sheet tab and you want to write their values on column C:
```py
from jersutils import get_eth_balances

ETHERSCAN_API_KEY = '123abcdef'
sheet1.update_list_values(
    sheet1.tabs[0], 'B', 'C',
    get_eth_balances, ETHERSCAN_API_KEY
)
```
The caveat for this is that you should have the first row as your header. As long as this requirement is met, you can have a list as long as you like, and even with gaps in between, and it should still work. But pls do let me know if it somehow doesn't!

Closing Thoughts
----------------
Thank you for reading and hopefully someone will find this useful! I am personally using it quite a bit myself! 😃 I believe this was also when I started getting into the habit of using .env files.. 😆

#### Notable libraries used / learned for this project:
- [Google API Client](https://pypi.org/project/google-api-python-client/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
