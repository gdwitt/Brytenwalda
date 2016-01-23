from source.header_operations import call_script


scripts = [
    ("initialize_trade_routes", [
        #SARGOTH - 10 routes
        (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_12"), #Sargoth - Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_11"), #Sargoth - Curaw
        (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_13"), #Sargoth - Rivacheg
        (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_14"), #Sargoth - Uxkhal
        (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_41"), #Sargoth - Khudan

        #TIHR- 8 Routes
        (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_6"), #Tihr - Praven
        (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_7"), #Tihr - Uxkhal
        (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_15"), #Tihr - Yalen
        (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_12"), #Tihr - Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_11"), #Tihr - Curaw

        #VELUCA - 8 Routes
        (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_5"), #Veluca - Jelkala
        (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_15"), #Veluca - Yalen
        (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_19"), #Veluca - Halmar
        (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_23"), #Veluca - Suno
        (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_32"), #Veluca - Shariz
        (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_37"), #Veluca - Praven

        #SUNO - 11 routes
        #Sargoth, Tihr, Veluca
        (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_12"), #Suno - Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_8"), #Suno - Reyvadin
        (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_7"), #Suno - Uxkhal
        (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_16"), #Suno - Dhirim
        (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_5"), #Suno - Jelkala

        #JELKALA - 6 ROUTES
        #Veluca, Suno
        (call_script, "script_set_trade_route_between_centers", "p_town_5", "p_town_15"), #Jelkala - Yalen
        (call_script, "script_set_trade_route_between_centers", "p_town_5", "p_town_6"), #Jelkala - Praven
        (call_script, "script_set_trade_route_between_centers", "p_town_5", "p_town_7"), #Jelkala - Uxkhal
        (call_script, "script_set_trade_route_between_centers", "p_town_5", "p_town_19"), #Jelkala - Shariz

        #PRAVEN - 7 ROUTES
        #Tihr, Veluca, Suno, Jelkala
        (call_script, "script_set_trade_route_between_centers", "p_town_6", "p_town_7"), #Praven - Uxkhal
        (call_script, "script_set_trade_route_between_centers", "p_town_6", "p_town_15"), #Praven - Yalen
        (call_script, "script_set_trade_route_between_centers", "p_town_6", "p_town_16"), #Praven - Dhirim

        #UXKHAL - 9 Routes
        #Sargoth, Tihr, Suno, Jelkala, Praven
        (call_script, "script_set_trade_route_between_centers", "p_town_7", "p_town_15"), #Yalen
        (call_script, "script_set_trade_route_between_centers", "p_town_7", "p_town_16"), #Dhirim
        (call_script, "script_set_trade_route_between_centers", "p_town_7", "p_town_19"), #Shariz
        (call_script, "script_set_trade_route_between_centers", "p_town_7", "p_town_14"), #Halmar

        #REYVADIN - 9 Routes
        #Suno, Sargoth
        (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_9"), #Khudan
        (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_12"), #Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_16"), #Dhirim
        (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_18"), #Narra
        (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_17"), #Ichamur

        #KHUDAN - 9 Routes
        #Sargoth, Reyvadin
        (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_11"), #Curaw
        (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_13"), #Rivacheg
        (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_12"), #Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_17"), #Ichamur
        (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_10"), #Tulga
        (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_16"), #Dhirim

        #TULGA - 7 Routes
        #Khudan
        (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_18"), #Narra
        (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_22"), #Bariyye
        (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_21"), #Ahmerrad
        (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_14"), #Halmar
        (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_20"), #Durquba

        #CURAW - 9 Routes
        #Khudan, Reyvadin, Sargoth, Suno
        (call_script, "script_set_trade_route_between_centers", "p_town_11", "p_town_12"), #Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_11", "p_town_13"), #Rivacheg
        (call_script, "script_set_trade_route_between_centers", "p_town_11", "p_town_14"), #Halmar
        (call_script, "script_set_trade_route_between_centers", "p_town_11", "p_town_16"), #Dhirim

        #WERCHEG - 7 Routes
        #Sargoth, Suno, Reyvadin, Khudan, Curaw, Tihr
        (call_script, "script_set_trade_route_between_centers", "p_town_12", "p_town_13"), #Rivacheg

        #RIVACHEG - 6 Routes
        #Sargoth, Reyvadin, Khudan, Curaw, Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_13", "p_town_17"), #Ichamur

        #HALMAR- 11 Routes
        #Veluca, Uxkhal, Tulga, Curaw
        (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_17"), #Ichamur
        (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_18"), #Narra
        (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_21"), #Ahmerrad
        (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_22"), #Bariyye
        (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_19"), #Shariz

        #YALEN - 7 Routes
        #Sargoth, Tihr, Veluca, Suno, Jelkala, Praven, Uxkhal

        #DHIRIM - 13 Routes
        #Sargoth, Thir, Veluca, Suno, Praven, Uxkhal, Reyvadin, Khudan, Curaw, Halmar
        (call_script, "script_set_trade_route_between_centers", "p_town_16", "p_town_18"), #Narra
        (call_script, "script_set_trade_route_between_centers", "p_town_16", "p_town_20"), #Durquba
        (call_script, "script_set_trade_route_between_centers", "p_town_16", "p_town_19"), #Shariz

        #ICHAMUR - 7 Routes
        #Reyvadin, Khudan, Tulga, Curaw, Rivacheg, Halmar
        (call_script, "script_set_trade_route_between_centers", "p_town_17", "p_town_18"), #Narra

        #NARRA - 9 Routes
        #Reyvadin, Khudan, Tulga, Halmar, Dhirim, Ichamur
        (call_script, "script_set_trade_route_between_centers", "p_town_18", "p_town_20"), #Durquba
        (call_script, "script_set_trade_route_between_centers", "p_town_18", "p_town_21"), #Ahmerrad
        (call_script, "script_set_trade_route_between_centers", "p_town_18", "p_town_22"), #Bariyye

        #SHARIZ - 8 Routes
        #Veluca, Jelkala, Uxkhal, Halmar, Dhirim
        (call_script, "script_set_trade_route_between_centers", "p_town_19", "p_town_20"), #Durquba
        (call_script, "script_set_trade_route_between_centers", "p_town_19", "p_town_21"), #Ahmerrad
        (call_script, "script_set_trade_route_between_centers", "p_town_19", "p_town_22"), #Bariyye

        #DURQUBA - 7 Routes
        #Tulga, Halmar, Dhirim, Narra, Shariz
        (call_script, "script_set_trade_route_between_centers", "p_town_20", "p_town_21"), #Ahmerrad
        (call_script, "script_set_trade_route_between_centers", "p_town_20", "p_town_22"), #Bariyye

        #AHMERRAD - 6 Routes
        #Tulga, Halmar, Narra, Shariz, Durquba
        (call_script, "script_set_trade_route_between_centers", "p_town_21", "p_town_22"), #Bariyye

        #BARIYYE - 6 Routes
        #Tulga, Halmar, Narra, Shariz, Durquba, Ahmerrad
        #Caer_Meguaidd - 10 routes
        (call_script, "script_set_trade_route_between_centers", "p_town_22", "p_town_25"), #Sargoth - Suno
        (call_script, "script_set_trade_route_between_centers", "p_town_22", "p_town_33"), #Sargoth - Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_22", "p_town_32"), #Sargoth - Curaw
        (call_script, "script_set_trade_route_between_centers", "p_town_22", "p_town_29"), #Sargoth - Reyvadin
        (call_script, "script_set_trade_route_between_centers", "p_town_22", "p_town_34"), #Sargoth - Rivacheg

        #Licidfelth- 8 Routes
        (call_script, "script_set_trade_route_between_centers", "p_town_23", "p_town_25"), #Tihr- Suno
        (call_script, "script_set_trade_route_between_centers", "p_town_23", "p_town_36"), #Tihr - Yalen
        (call_script, "script_set_trade_route_between_centers", "p_town_23", "p_town_33"), #Tihr - Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_23", "p_town_29"), #Tihr - Reyvadin
        (call_script, "script_set_trade_route_between_centers", "p_town_23", "p_town_37"), #Thir - Dhirim

        #VELUCA - 8 Routes
        (call_script, "script_set_trade_route_between_centers", "p_town_24", "p_town_28"), #Veluca- Uxkhal
        (call_script, "script_set_trade_route_between_centers", "p_town_24", "p_town_36"), #Veluca - Jelkala
        (call_script, "script_set_trade_route_between_centers", "p_town_24", "p_town_40"), #Veluca - Halmar
        (call_script, "script_set_trade_route_between_centers", "p_town_24", "p_town_34"), #Veluca - Suno
        (call_script, "script_set_trade_route_between_centers", "p_town_24", "p_town_41"), #Veluca - Shariz

        #SUNO - 11 routes
        #Sargoth, Tihr, Veluca
        (call_script, "script_set_trade_route_between_centers", "p_town_25", "p_town_33"), #Suno - Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_25", "p_town_27"), #Suno - Praven
        (call_script, "script_set_trade_route_between_centers", "p_town_25", "p_town_28"), #Suno - Uxkhal
        (call_script, "script_set_trade_route_between_centers", "p_town_25", "p_town_26"), #Suno - Jelkala
        (call_script, "script_set_trade_route_between_centers", "p_town_25", "p_town_36"), #Suno - Yalen

        #JELKALA - 6 ROUTES
        #Veluca, Suno
        (call_script, "script_set_trade_route_between_centers", "p_town_26", "p_town_36"), #Jelkala - Yalen
        (call_script, "script_set_trade_route_between_centers", "p_town_26", "p_town_37"), #Jelkala - Praven
        (call_script, "script_set_trade_route_between_centers", "p_town_26", "p_town_38"), #Jelkala - Uxkhal
        (call_script, "script_set_trade_route_between_centers", "p_town_26", "p_town_40"), #Jelkala - Shariz

        #PRAVEN - 7 ROUTES
        #Tihr, Veluca, Suno, Jelkala
        (call_script, "script_set_trade_route_between_centers", "p_town_27", "p_town_28"), #Praven - Uxkhal
        (call_script, "script_set_trade_route_between_centers", "p_town_27", "p_town_36"), #Praven - Yalen
        (call_script, "script_set_trade_route_between_centers", "p_town_27", "p_town_37"), #Praven - Dhirim

        #UXKHAL - 9 Routes
        #Sargoth, Tihr, Suno, Jelkala, Praven
        (call_script, "script_set_trade_route_between_centers", "p_town_28", "p_town_36"), #Yalen
        (call_script, "script_set_trade_route_between_centers", "p_town_28", "p_town_37"), #Dhirim
        (call_script, "script_set_trade_route_between_centers", "p_town_28", "p_town_40"), #Shariz
        (call_script, "script_set_trade_route_between_centers", "p_town_28", "p_town_35"), #Halmar

        #REYVADIN - 9 Routes
        #Suno, Sargoth
        (call_script, "script_set_trade_route_between_centers", "p_town_29", "p_town_32"), #Curaw
        (call_script, "script_set_trade_route_between_centers", "p_town_29", "p_town_33"), #Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_29", "p_town_37"), #Dhirim
        (call_script, "script_set_trade_route_between_centers", "p_town_29", "p_town_39"), #Narra
        (call_script, "script_set_trade_route_between_centers", "p_town_29", "p_town_38"), #Ichamur

        #KHUDAN - 9 Routes
        #Sargoth, Reyvadin
        (call_script, "script_set_trade_route_between_centers", "p_town_30", "p_town_34"), #Rivacheg
        (call_script, "script_set_trade_route_between_centers", "p_town_30", "p_town_33"), #Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_30", "p_town_38"), #Ichamur
        (call_script, "script_set_trade_route_between_centers", "p_town_30", "p_town_31"), #Tulga

        #TULGA - 7 Routes
        #Khudan
        (call_script, "script_set_trade_route_between_centers", "p_town_31", "p_town_28"), #Ichamur
        (call_script, "script_set_trade_route_between_centers", "p_town_31", "p_town_39"), #Narra
        (call_script, "script_set_trade_route_between_centers", "p_town_31", "p_town_42"), #Bariyye
        (call_script, "script_set_trade_route_between_centers", "p_town_31", "p_town_41"), #Durquba

        #CURAW - 9 Routes
        #Khudan, Reyvadin, Sargoth, Suno
        (call_script, "script_set_trade_route_between_centers", "p_town_32", "p_town_33"), #Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_32", "p_town_35"), #Halmar
        (call_script, "script_set_trade_route_between_centers", "p_town_32", "p_town_37"), #Dhirim
        (call_script, "script_set_trade_route_between_centers", "p_town_32", "p_town_38"), #Ichamur

        #WERCHEG - 7 Routes
        #Sargoth, Suno, Reyvadin, Khudan, Curaw, Tihr
        (call_script, "script_set_trade_route_between_centers", "p_town_33", "p_town_34"), #Rivacheg

        #RIVACHEG - 6 Routes
        #Sargoth, Reyvadin, Khudan, Curaw, Wercheg
        (call_script, "script_set_trade_route_between_centers", "p_town_34", "p_town_38"), #Ichamur

        #HALMAR- 11 Routes
        #Veluca, Uxkhal, Tulga, Curaw
        (call_script, "script_set_trade_route_between_centers", "p_town_35", "p_town_41"), #Ahmerrad
        (call_script, "script_set_trade_route_between_centers", "p_town_35", "p_town_40"), #Bariyye
        (call_script, "script_set_trade_route_between_centers", "p_town_35", "p_town_42"), #Durquba
        (call_script, "script_set_trade_route_between_centers", "p_town_35", "p_town_39"), #Shariz

        #YALEN - 7 Routes
        #Sargoth, Tihr, Veluca, Suno, Jelkala, Praven, Uxkhal

        #DHIRIM - 13 Routes
        #Sargoth, Thir, Veluca, Suno, Praven, Uxkhal, Reyvadin, Khudan, Curaw, Halmar
        (call_script, "script_set_trade_route_between_centers", "p_town_36", "p_town_41"), #Durquba
        (call_script, "script_set_trade_route_between_centers", "p_town_36", "p_town_40"), #Shariz

        #ICHAMUR - 7 Routes
        #Reyvadin, Khudan, Tulga, Curaw, Rivacheg, Halmar
        (call_script, "script_set_trade_route_between_centers", "p_town_37", "p_town_39"), #Narra

        #NARRA - 9 Routes
        #Reyvadin, Khudan, Tulga, Halmar, Dhirim, Ichamur
        (call_script, "script_set_trade_route_between_centers", "p_town_38", "p_town_41"), #Durquba
        (call_script, "script_set_trade_route_between_centers", "p_town_38", "p_town_42"), #Ahmerrad
        (call_script, "script_set_trade_route_between_centers", "p_town_38", "p_town_40"), #Bariyye

        #SHARIZ - 8 Routes
        #Veluca, Jelkala, Uxkhal, Halmar, Dhirim
        (call_script, "script_set_trade_route_between_centers", "p_town_39", "p_town_40"), #Durquba
        (call_script, "script_set_trade_route_between_centers", "p_town_39", "p_town_41"), #Ahmerrad
        (call_script, "script_set_trade_route_between_centers", "p_town_39", "p_town_42"), #Bariyye

        #DURQUBA - 7 Routes
        #Tulga, Halmar, Dhirim, Narra, Shariz
        (call_script, "script_set_trade_route_between_centers", "p_town_40", "p_town_41"), #Ahmerrad
        (call_script, "script_set_trade_route_between_centers", "p_town_40", "p_town_42"), #Bariyye

        #AHMERRAD - 6 Routes
        #Tulga, Halmar, Narra, Shariz, Durquba
        (call_script, "script_set_trade_route_between_centers", "p_town_41", "p_town_42"), #Bariyye

        #BARIYYE - 6 Routes
        #Tulga, Halmar, Narra, Shariz, Durquba, Ahmerrad
    ]),
]
