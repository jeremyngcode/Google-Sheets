from googleapiclient import discovery
from google.oauth2 import service_account
# -------------------------------------------------------------------------------------------------

class Sheet:
	def __init__(self, google_creds_path, spreadsheet_id, *sheet_tabs):
		creds = service_account.Credentials.from_service_account_file(google_creds_path)
		self.service = discovery.build('sheets', 'v4', credentials=creds)

		self.spreadsheet_id = spreadsheet_id
		self.tabs = sheet_tabs

	def get_values(self, sheet_tab, cells_range):
		result = self.service.spreadsheets().values().get(
			spreadsheetId=self.spreadsheet_id,
			range=f'{sheet_tab}!{cells_range}'
		).execute()

		print(f'get_values(): {result}')
		return result.get('values')

	def update_values(self, sheet_tab, cells_range, values):
		body = {
			'values': values
		}
		result = self.service.spreadsheets().values().update(
			spreadsheetId=self.spreadsheet_id,
			range=f'{sheet_tab}!{cells_range}',
			valueInputOption='USER_ENTERED',
			body=body
		).execute()

		print(f'update_values(): {result}')
		return result

	def update_list_values(self, sheet_tab, list_col, values_col,
		func, *KEYS):
		items = self.get_values(
			sheet_tab=sheet_tab,
			cells_range=f'{list_col}:{list_col}'
		)

		item_list = []
		for item in items[1:]:
			if item:
				item_list.append(item[0])
			else:
				item_list.append('')
		print()

		if KEYS:
			retrieved_values = func(*KEYS, *item_list)
		else:
			retrieved_values = func(*item_list)

		if retrieved_values is None:
			return

		values = []
		for item in item_list:
			if retrieved_values.get(item):
				values.append([retrieved_values[item]])
			else:
				values.append([])

		cells_range = f'{values_col}2:{values_col}{len(values) + 1}'

		self.update_values(
			sheet_tab=sheet_tab,
			cells_range=cells_range,
			values=values
		)
