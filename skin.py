import pymem, pymem.process
import keyboard
import json
import requests

# auto-update offsets
print("Getting offsets, hang on a sec...\n-----------------")
t = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json")
dwLocalPlayer = int(t.json()['signatures']['dwLocalPlayer'])
m_hMyWeapons = int(t.json()['netvars']['m_hMyWeapons'])
dwEntityList = int(t.json()['signatures']['dwEntityList'])
m_iItemIDHigh = int(t.json()['netvars']['m_iItemIDHigh'])
dwClientState = int(t.json()['signatures']['dwClientState'])
m_nFallbackPaintKit = int(t.json()['netvars']['m_nFallbackPaintKit'])
m_iItemDefinitionIndex = int(t.json()['netvars']['m_iItemDefinitionIndex'])
m_flFallbackWear = int(t.json()['netvars']['m_flFallbackWear'])
m_nFallbackStatTrak = int(t.json()['netvars']['m_nFallbackStatTrak'])
print("Skin swapper has launched.")
handle = pymem.Pymem("csgo.exe")
client_dll = pymem.process.module_from_name(handle.process_handle, "client.dll").lpBaseOfDll
engine_dll = pymem.process.module_from_name(handle.process_handle, "engine.dll").lpBaseOfDll

def force_full_update():
    engine_state = handle.read_int(engine_dll + dwClientState)
    handle.write_int(engine_state + 0x174, -1)

def statTrak(value):
    handle.write_int(currentWeapon + m_nFallbackStatTrak, value)

while True:
    f = open('config.json', "r")
    config = json.load(f)

    localPlayer = handle.read_int(client_dll + dwLocalPlayer)
    for i in range(8):
        currentWeapon = handle.read_int(localPlayer + m_hMyWeapons + i * 0x4) & 0xfff
        currentWeapon = handle.read_int(client_dll + dwEntityList + (currentWeapon - 1) * 0x10)
        if currentWeapon == 0:
            continue

        weaponID = handle.read_short(currentWeapon + m_iItemDefinitionIndex)
        fallbackPaint = 0
        fallbackWear = 0.01
        itemIDHigh = -1

        for (k, v) in config.items():
            if weaponID == config[k]["id"]:
                fallbackPaint = config[k]["skinID"]
                fallbackWear = config[k]["float"]
                if "statTrack" in config[k]:
                    statTrak(config[k]["statTrack"])
        handle.write_int(currentWeapon + m_iItemIDHigh, itemIDHigh)
        handle.write_int(currentWeapon + m_nFallbackPaintKit, fallbackPaint)
        handle.write_float(currentWeapon + m_flFallbackWear, fallbackWear)
        
        if keyboard.is_pressed('f1'):
            force_full_update()