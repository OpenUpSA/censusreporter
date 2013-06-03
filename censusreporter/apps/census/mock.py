PROFILE_TEST = {
    "geography": {
        "sumlev": "060",
        "census_name": "Spokane",
        "pretty_name": "Spokane County, Washington",
        "stusab": "53",
        "total_population": "2345987",
        "land_area": "1298345",
        "census_release": "ACS 2011 1-year"
    },
    
    "demographics": {
        "age": {
            "percent_under_18": {
                "table_id": "B01001",
                "universe": "Total population",
                "name": "Under 18",
                "values": {
                    "geography": "28.2",
                    "parent_county": None,
                    "parent_state": "27.3",
                    "parent_nation": "27.8"
                }
            },
            "percent_65_over": {
                "table_id": "B01001",
                "universe": "Total population",
                "name": "65 and over",
                "values": {
                    "geography": "13.1",
                    "parent_county": None,
                    "parent_state": "12.5",
                    "parent_nation": "12.6"
                }
            }
        },
        "gender": {
            "percent_male": {
                "table_id": "B01001",
                "universe": "Total population",
                "name": "Male",
                "values": {
                    "geography": "48.1",
                    "parent_county": None,
                    "parent_state": "48.7",
                    "parent_nation": "49.5"
                }
            },
            "percent_female": {
                "table_id": "B01001",
                "universe": "Total population",
                "name": "Female",
                "values": {
                    "geography": "51.9",
                    "parent_county": None,
                    "parent_state": "51.3",
                    "parent_nation": "50.5"
                }
            }
        },
        "race": {
            "percent_white": {
                "table_id": "B02001",
                "universe": "Total population",
                "name": "White",
                "values": {
                    "geography": "87.5",
                    "parent_county": None,
                    "parent_state": "79.2",
                    "parent_nation": "81.3"
                }
            },
            "percent_black": {
                "table_id": "B02001",
                "universe": "Total population",
                "name": "Black",
                "values": {
                    "geography": "12.3",
                    "parent_county": None,
                    "parent_state": "12.2",
                    "parent_nation": "13.1"
                }
            },
            "percent_american_indian": {
                "table_id": "B02001",
                "universe": "Total population",
                "name": "Native",
                "values": {
                    "geography": "1.1",
                    "parent_county": None,
                    "parent_state": "1.5",
                    "parent_nation": "1.3"
                }
            },
            "percent_asian": {
                "table_id": "B02001",
                "universe": "Total population",
                "name": "Asian",
                "values": {
                    "geography": "3.3",
                    "parent_county": None,
                    "parent_state": "3.8",
                    "parent_nation": "3.6"
                }
            },
            "percent_islander": {
                "table_id": "B02001",
                "universe": "Total population",
                "name": "Islander",
                "values": {
                    "geography": "1.2",
                    "parent_county": None,
                    "parent_state": "1.9",
                    "parent_nation": "1.7"
                }
            },
            "percent_other": {
                "table_id": "B02001",
                "universe": "Total population",
                "name": "Other race",
                "values": {
                    "geography": "1.7",
                    "parent_county": None,
                    "parent_state": "1.9",
                    "parent_nation": "1.8"
                }
            },
            "percent_two_or_more": {
                "table_id": "B02001",
                "universe": "Total population",
                "name": "Two+ races",
                "values": {
                    "geography": "1.0",
                    "parent_county": None,
                    "parent_state": "0.8",
                    "parent_nation": "0.9"
                }
            }
        },
        "ethnicity": {
            "percent_hispanic": {
                "table_id": "B03001",
                "universe": "Total population",
                "name": "Hispanic/Latino",
                "values": {
                    "geography": "11.5",
                    "parent_county": None,
                    "parent_state": "11.5",
                    "parent_nation": "11.7"
                }
            }
        }
    },
    
    "economics": {
        "income": {
            "per_capita_income": {
                "table_id": "B19301",
                "universe": "Total population",
                "name": "Per capita income in past year",
                "values": {
                    "geography": "34982",
                    "parent_county": None,
                    "parent_state": "37482",
                    "parent_nation": "36904"
                }
            },
            "median_household_income": {
                "table_id": "B19013",
                "name": "Median household income",
                "universe": "Households",
                "values": {
                    "geography": "41184",
                    "parent_county": None,
                    "parent_state": "42087",
                    "parent_nation": "42113"
                }
            }
        },
        "poverty": {
            "percent_poverty": {
                "table_id": "B17001",
                "universe": "Population for whom poverty status is determined",
                "name": "People below poverty line",
                "values": {
                    "geography": "20.1",
                    "parent_county": None,
                    "parent_state": "19.8",
                    "parent_nation": "21.6"
                }
            }
        }
    },

    "education": {
        "attainment": {
            "percent_high_school": {
                "table_id": "B15002",
                "universe": "Population 25 years and over",
                "name": "High school grad or higher",
                "values": {
                    "geography": "74.9",
                    "parent_county": None,
                    "parent_state": "77.3",
                    "parent_nation": "76.3"
                }
            },
            "percent_college": {
                "table_id": "B15002",
                "universe": "Population 25 years and over",
                "name": "Bachelor's degree or higher",
                "values": {
                    "geography": "43.2",
                    "parent_county": None,
                    "parent_state": "47.2",
                    "parent_nation": "39.7"
                }
            }
        }
    },
    
    "employment": {
        "travel_time": {
            "mean_travel_time": {
                "table_id": "B08006, B08013",
                "universe": "Workers 16 years and over",
                "name": "Mean travel time to work",
                "values": {
                    "geography": "27.6",
                    "parent_county": None,
                    "parent_state": "28.2",
                    "parent_nation": "29.9"
                }
            }
        }
    },
    
    "families": {
        "households": {
            "number_households": {
                "table_id": "B11001",
                "universe": "Households",
                "name": "Number of households",
                "values": {
                    "geography": "43092",
                    "parent_county": None,
                    "parent_state": "576231",
                    "parent_nation": "9834627"
                }
            },
            "persons_per_household": {
                "table_id": "B11001, B11002",
                "universe": "Households",
                "name": "Persons per household",
                "values": {
                    "geography": "3.2",
                    "parent_county": None,
                    "parent_state": "3.8",
                    "parent_nation": "3.7"
                }
            }
        }
    },
    
    "health": {},

    "housing": {
        "housing_units": {
            "number_housing_units": {
                "table_id": "B25001",
                "universe": "Housing units",
                "name": "Number of housing units",
                "values": {
                    "geography": "139824",
                    "parent_county": None,
                    "parent_state": "223765",
                    "parent_nation": "1098364"
                }
            },
            "percent_multi_unit": {
                "table_id": "B25024",
                "universe": "Housing units",
                "name": "Housing units in multi-unit structures",
                "values": {
                    "geography": "38.7",
                    "parent_county": None,
                    "parent_state": "22.9",
                    "parent_nation": "32.1"
                }
            }
        },
        "tenure": {
            "rate_homeownership": {
                "table_id": "B25003",
                "universe": "Occupied housing units",
                "name": "Rate of homeownership",
                "values": {
                    "geography": "45.6",
                    "parent_county": None,
                    "parent_state": "45.5",
                    "parent_nation": "44.1"
                }
            }
        },
        "value": {
            "median_value": {
                "table_id": "B25077",
                "universe": "Owner-occupied housing units",
                "name": "Median value of owner-occupied housing units",
                "values": {
                    "geography": "213945",
                    "parent_county": None,
                    "parent_state": "201934",
                    "parent_nation": "207553"
                }
            }
        },
        "mobility": {
            "percent_same_house": {
                "table_id": "B07001",
                "universe": "Population 1 year and over in the United States",
                "name": "People living in same house for 1 year or more",
                "values": {
                    "geography": "38.1",
                    "parent_county": None,
                    "parent_state": "39.0",
                    "parent_nation": "40.9"
                }
            }
        }
    },

    "sociocultural": {
        "place_of_birth": {
            "percent_foreign_born": {
                "table_id": "B05002",
                "universe": "Total population",
                "name": "Foreign-born persons",
                "values": {
                    "geography": "22.5",
                    "parent_county": None,
                    "parent_state": "19.4",
                    "parent_nation": "25.7"
                }
            }
        },
        "language": {
            "percent_non_english_at_home": {
                "table_id": "B16001",
                "universe": "Population 5 years and over",
                "name": "People with language other than English spoken at home",
                "values": {
                    "geography": "9.3",
                    "parent_county": None,
                    "parent_state": "9.7",
                    "parent_nation": "11.2"
                }
            }
        }
    },

    "veterans": {
        "veteran_status": {
            "number_veterans": {
                "table_id": "B21002",
                "universe": "Civilian veterans 18 years and over",
                "name": "Number of veterans",
                "values": {
                    "geography": "4983",
                    "parent_county": None,
                    "parent_state": "52015",
                    "parent_nation": "1099374"
                }
            }
        }
    }
}