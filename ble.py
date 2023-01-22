### To discover Bluetooth LE(low energy) devices that can be connected to: ###
import asyncio
from bleak import BleakScanner, BleakClient
import logging
logger = logging.getLogger(__name__)

# import bitstruct
# import struct




async def main():
	print("Scanning...")
	devices = await BleakScanner.discover()
	for device in devices:
		print("...................................................")
		print(device.address, device.name)
		#d.details = {'path': '/org/bluez/hci0/dev_DE_BD_78_CF_7E_CB', 'props': {'Address': 'DE:BD:78:CF:7E:CB', 'AddressType': 'random', 'Name': 'ID115Plus HR', 'Alias': 'ID115Plus HR', 'Paired': False, 'Trusted': False, 'Blocked': False, 'LegacyPairing': False, 'Connected': False, 'UUIDs': ['00000af0-0000-1000-8000-00805f9b34fb', '00001800-0000-1000-8000-00805f9b34fb', '00001801-0000-1000-8000-00805f9b34fb'], 'Adapter': '/org/bluez/hci0', 'ServicesResolved': False, 'RSSI': -48}}
		print("Details ------->: ", device.details)

		###
		# async with BleakClient(device, timeout=60, use_cached=False) as client:
		# 	services = await client.get_services()
		# 	for service in services:
		# 		print('\nservice', service.handle, service.uuid, service.description)

		# 		characteristics = service.characteristics

		# 		for char in characteristics:
		# 			print('  characteristic', char.handle, char.uuid, char.description, char.properties)

		# 			descriptors = char.descriptors

		# 			for desc in descriptors:
		# 				print('    descriptor', desc)

		####


asyncio.run(main())



# # ## Connect to a Bluetooth device and read its model number: ##
# # import asyncio
# # from bleak import BleakClient

# #DE:BD:78:CF:7E:CB = ID115plus HR
# address = "D4:3A:2C:6C:34:7D"
# # MODEL_NBR_UUID = "00000af6-0000-1000-8000-00805f9b34fb" #"00002a24-0000-1000-8000-00805f9b34fb"
# # HR_MEAS = "00000af2-0000-1000-8000-00805f9b34fb" #
# # HR_MEAS = "00000af7-0000-1000-8000-00805F9B34FB" #
# # TIME_CHAR = "00000af6-0000-1000-8000-00805f9b34fb"


# # def hr_val_handler(data):
# # 	"""Simple notification handler for Heart Rate Measurement."""
# # 	print("HR Measurement raw = %s"%data)
# # 	(hr_fmt,
# # 		snsr_detect,
# # 		snsr_cntct_spprtd,
# # 		nrg_expnd,
# # 		rr_int) = bitstruct.unpack("b1b1b1b1b1<", data)
# # 	if hr_fmt:
# # 		hr_val, = struct.unpack_from("<H", data, 1)
# # 	else:
# # 		hr_val, = struct.unpack_from("<B", data, 1)
# # 	print(f"HR Value: {hr_val}")


# async def main(address):
# 	device = await BleakScanner.find_device_by_address(address, timeout=60)
# 	# async with BleakClient(address) as client:
# 	if device:
# 		print(device.address, device.name)
# 		async with BleakClient(device, timeout=60, use_cached=False) as client:

# 			# await client.write_gatt_char(TIME_CHAR, data="020129021b0100580100".tobytes(), response=True)

# 			# data_bytes = await client.read_gatt_char("00000af7-0000-1000-8000-00805F9B34FB")
# 			# data = bytearray.decode(data_bytes)
# 			# print('data', data)

# 			# ##################
# 			services = await client.get_services()
# 			for service in services:
# 				print('\nservice', service.handle, service.uuid, service.description)

# 				characteristics = service.characteristics

# 				for char in characteristics:
# 					print('  characteristic', char.handle, char.uuid, char.description, char.properties)

# 					descriptors = char.descriptors

# 					for desc in descriptors:
# 						print('    descriptor', desc)
# 			# ###############

# 			# ##########

# 			# connected = await client.is_connected()
# 			# print("Connected: {0}".format(connected))

# 			# def hr_val_handler(sender, data):
# 			# 	"""Simple notification handler for Heart Rate Measurement."""
# 			# 	print("HR Measurement raw = {0}: {1}".format(sender, data))
# 			# 	(hr_fmt,
# 			# 	snsr_detect,
# 			# 	snsr_cntct_spprtd,
# 			# 	nrg_expnd,
# 			# 	rr_int) = bitstruct.unpack("b1b1b1b1b1<", data)
# 			# 	if hr_fmt:
# 			# 		hr_val, = struct.unpack_from("<H", data, 1)
# 			# 	else:
# 			# 		hr_val, = struct.unpack_from("<B", data, 1)
# 			# 	print(f"HR Value: {hr_val}")

# 			# await client.start_notify(HR_MEAS, hr_val_handler)

# 			# while await client.is_connected():
# 			# 	await asyncio.sleep(1)

# 			# ##########


# 			# model_number = await client.read_gatt_char(MODEL_NBR_UUID)
# 			# print("Model Number: {0}".format("".join(map(chr, model_number))))

# 	else:
# 		print("Device not found")


# asyncio.run(main(address))