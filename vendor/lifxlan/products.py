# coding=utf-8
product_map = {1: "Original 1000",
               3: "Color 650",
               10: "White 800 (Low Voltage)",
               11: "White 800 (High Voltage)",
               18: "White 900 BR30 (Low Voltage)",
               20: "Color 1000 BR30",
               22: "Color 1000",
               27: "LIFX A19",
               28: "LIFX BR30",
               29: "LIFX+ A19",
               30: "LIFX+ BR30",
               31: "LIFX Z"
               }
               
# Identifies which products are lights.
# Currently all LIFX products that speak the LAN protocol are lights.
# However, the protocol was written to allow addition of other kinds
# of devices, so it's important to be able to differentiate.
light_products = [1, 3, 10, 11, 18, 20, 22, 27, 28, 29, 30, 31]

features_map = {1: {"color": True,
                    "infrared": False,
                    "multizone": False},
                3: {"color": True,
                    "infrared": False,
                    "multizone": False},
                10: {"color": False,
                     "infrared": False,
                     "multizone": False},
                11: {"color": False,
                     "infrared": False,
                     "multizone": False},
                18: {"color": False,
                     "infrared": False,
                     "multizone": False},
                20: {"color": True,
                     "infrared": False,
                     "multizone": False},
                22: {"color": True,
                     "infrared": False,
                     "multizone": False},
                27: {"color": True,
                     "infrared": False,
                     "multizone": False},
                28: {"color": True,
                     "infrared": False,
                     "multizone": False},
                29: {"color": True,
                     "infrared": True,
                     "multizone": False},
                30: {"color": True,
                     "infrared": True,
                     "multizone": False},
                31: {"color": True,
                     "infrared": False,
                     "multizone": True}
                }
