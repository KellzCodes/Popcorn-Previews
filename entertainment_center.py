import media
import fresh_tomatoes

"""
Creates various instances of the classes Movie and Show.
"""

godfather = media.Movie("The Godfather", "2h 58m ", True, False,
                        "The aging patriarch of a crime dynasty"
                        "\ntransfers control of his empire to his"
                        "\nreluctant son.",  # noqa
                        "Francis Ford Coppola", "Paramount Pictures",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",  # noqa
                        "https://www.youtube.com/watch?v=sY1S34973zA")

fresh = media.Movie("Fresh", "1h 55m ", True, False,
                    "In a world where criminals make the rules, a 12 year old "
                    "\nboy is out to beat them at their own game.",  # noqa
                    "Boaz Yakin", "Miramax",  # noqa
                    "https://upload.wikimedia.org/wikipedia/en/c/cd/Fresh_movie_90s.jpg",  # noqa
                    "https://www.youtube.com/watch?v=y7QvSl4C4hE")

higher_learning = media.Movie("Higher Learning", "2h 8m ", True, False,
                              "People, from all different walks of life, "
                              "encounter racial tension, "
                              "\nrape, responsibility, and the meaning of an "
                              "education on a" + "\nuniversity campus.",
                              "John Singleton",
                              "Columbia Pictures",
                              "https://upload.wikimedia.org/wikipedia/en/2/26/Higher_Learning_%28movie%29.jpg",  # noqa
                              "https://www.youtube.com/watch?v=_4KVCVX1MrQ")

hotel_transylvania_2 = media.Movie("Hotel Transylvania 2", "1h 29m ",
                                   True, False,  # noqa
                                   "Dracula and his friends try to bring out "
                                   "the monster in his half human "
                                   "\nhalf vampire grandson in order to keep "
                                   "Mavis from leaving the hotel.",
                                   "Genndy Tartakovsky",
                                   "Columbia Pictures",
                                   "https://upload.wikimedia.org/wikipedia/en/5/5d/Hotel_Transylvania_2_poster.jpg",  # noqa
                                   "https://www.youtube.com/watch?v=T3nqmGgnJe8")  # noqa

lion_king = media.Movie("The Lion King", "1h 29m ", True, False,
                        "Lion cub and future king Simba searches for his "
                        "identity \nHis eagerness to please others and "
                        "penchant for testing his \nboundaries sometimes gets "
                        "him into trouble.", "Roger Allers and Rob Minkoff",
                        "Walt Disney Pictures",  # noqa
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

cinderella = media.Movie("Cinderella", "1h 28m ", True, False,
                         "Updated version of the classic Rodgers and "
                         "Hammerstein musical \nof the classic fairy-tale, "
                         "with an all-star, multi-racial cast.",
                         "Robert Iscove", "BrownHouse Productions",
                         "https://upload.wikimedia.org/wikipedia/en/f/f8/Cind_1997.jpg",  # noqa
                         "https://www.youtube.com/watch?v=EOKDuFW6XFo")

kill_bill = media.Movie("Kill Bill: Vol. 1", "1h 51m", True, False,
                        "The Bride wakens from a four-year coma. The child "
                        "she carried in her womb is gone. Now she \nmust "
                        "wreak vengeance on the team of assassins who "
                        "betrayed her.", "Quentin Tarantino", "A Band Apart",
                        "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",  # noqa
                        "https://www.youtube.com/watch?v=ot6C1ZKyiME")

color_purple = media.Movie("The Color Purple", "2h 34m", True, False,
                           "A black Southern woman struggles to find her "
                           "identity after suffering abuse from her \nfather "
                           "and others over four decades.", "Steven Spielberg",
                           "Warner Brothers",  # noqa
                           "https://upload.wikimedia.org/wikipedia/en/b/be/The_Color_Purple_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=d83NnlL83mc")

nightmare = media.Movie("The Nightmare Before Christmas", "1h 16m", True, False,  # noqa
                        "Jack Skellington, king of Halloween Town, discovers"
                        " Christmas Town, but doesn't quite \nunderstand "
                        "the concept.", "Henry Selick", "Touchstone Pictures",
                        "https://upload.wikimedia.org/wikipedia/en/9/9a/The_nightmare_before_christmas_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=wr6N_hZyBCk")

scrubs = media.Show("Scrubs", "Season 3", False, True, "22 Episodes ",
                    "In the unreal world of Sacred Heart Hospital, Dr. "
                    "John 'JD' Dorian learns \nthe ways of medicine, "
                    "friendship and life.", "ABC",  # noqa
                    "https://upload.wikimedia.org/wikipedia/en/4/45/Scrubs-s3-dvd.jpg",  # noqa
                    "https://www.youtube.com/watch?v=do9jR8Guz_E")

ahs_coven = media.Show("American Horror Story: Coven", "Season 3", False, True,
                       "13 Episodes ", "After discovering her unique bloodline"
                       ", a young girl is whisked \naway to a special academy"
                       " for girls who share the same lineage.", "FX",  # noqa
                       "https://upload.wikimedia.org/wikipedia/en/b/b2/American_Horror_Story_Season_3.jpg",  # noqa
                       "https://www.youtube.com/watch?v=NQRPiNRGoF8")

ahs_murder_house = media.Show("American Horror Story: Murder House", "Season 1",  # noqa
                              False, True, "12 Episodes ", "Therapist Ben"
                              " Harmon, his wife, Vivien, and their \ndaughter"
                              ", Violet, move across the country to Los"
                              "\nAngeles to escape their troubled past.",
                              "FX", "https://upload.wikimedia.org/wikipedia/en/e/eb/American_Horror_Story_Season_1.jpg",  # noqa
                              "https://www.youtube.com/watch?v=-9KZr2Vn7CQ")

will_grace = media.Show("Will & Grace", "Season 6", False, True, "24 Episodes ",  # noqa
                        "Will and Grace live together in an apartment in "
                        "New York. He's a gay lawyer, \nshe's a straight"
                        " interior designer.", "NBC",
                        "https://upload.wikimedia.org/wikipedia/en/0/01/Will_%26_Grace_Season_6.jpg",  # noqa
                        "https://www.youtube.com/watch?v=PbmZ39kEwGM")

oz = media.Show("Oz", "Season 2", False, True, "8 Episodes ",
                "In the aftermath of the riot that"
                "\nkilled six inmates and two officers,"
                "\nOz is locked down, and Emerald City prisoners"
                "\nare sent either to solitary or gen pop. A special"
                "\ncommittee is appointed to investigate the riot.",
                "HBO", "https://upload.wikimedia.org/wikipedia/en/9/9d/Ozposter.jpg",  # noqa
                "https://www.youtube.com/watch?v=F00xQE1DdXo")

desperate_housewives = media.Show("Desperate Housewives", "Season 8", False,
                                  True, "24 Episodes ",  # noqa
                                  "Secrets and truths unfold through the lives"
                                  " of female friends \nin one suburban"
                                  " neighborhood, after the mysterious suicide"
                                  " of a neighbor.", "ABC",  # noqa
                                  "https://upload.wikimedia.org/wikipedia/en/4/4a/DHWS8Promo.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=GVBCqGtkvvA")  # noqa

boondocks = media.Show("The Boondocks", "Season 2", False, True, "15 Episodes",
                       "Huey and Riley move away from the city and out to the"
                       " suburbs with their irascible \ngrandfather.",  # noqa
                       "Adult Swim",  # noqa
                       "https://upload.wikimedia.org/wikipedia/en/f/f6/Boondocks_season_2_DVD.png",  # noqa
                       "https://www.youtube.com/watch?v=FTMHx6JuQDw")

simpsons = media.Show("The Simpsons", "Season 17", False, True, "22 Episodes",
                      "The satiric adventures of a working-class family in the"
                      " misfit city of Springfield.", "Fox",
                      "https://upload.wikimedia.org/wikipedia/en/c/cf/The_Simpsons_-_The_17th_Season.jpg",  # noqa
                      "https://www.youtube.com/watch?v=R9fmstvhzog")

family_guy = media.Show("Family Guy", "Season 14", False, True, "20 Episodes",
                        "In a wacky Rhode Island town, a dysfunctional family"
                        " strive to cope with everyday life \nas they are"
                        " thrown from one crazy scenario to another.", "Fox",
                        "https://upload.wikimedia.org/wikipedia/en/4/49/Family_Guy_%28season_14%29.jpg",  # noqa
                        "https://www.youtube.com/watch?v=rB_VUVUA_QI")

# Put video objects in an array
videos = [godfather, fresh, scrubs, oz, cinderella, will_grace,  # noqa
          desperate_housewives, lion_king, hotel_transylvania_2,  # noqa
          higher_learning, ahs_coven, ahs_murder_house, boondocks,  # noqa
          kill_bill, color_purple, simpsons, family_guy, nightmare]

import media
import fresh_tomatoes

"""
Creates various instances of the classes Movie and Show.
"""

godfather = media.Movie("The Godfather", "2h 58m ", True, False,
                        "The aging patriarch of a crime dynasty"
                        "\ntransfers control of his empire to his"
                        "\nreluctant son.",  # noqa
                        "Francis Ford Coppola", "Paramount Pictures",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",  # noqa
                        "https://www.youtube.com/watch?v=sY1S34973zA")

fresh = media.Movie("Fresh", "1h 55m ", True, False,
                    "In a world where criminals make the rules, a 12 year old "
                    "\nboy is out to beat them at their own game.",  # noqa
                    "Boaz Yakin", "Miramax",  # noqa
                    "https://upload.wikimedia.org/wikipedia/en/c/cd/Fresh_movie_90s.jpg",  # noqa
                    "https://www.youtube.com/watch?v=y7QvSl4C4hE")

higher_learning = media.Movie("Higher Learning", "2h 8m ", True, False,
                              "People, from all different walks of life, "
                              "encounter racial tension, "
                              "\nrape, responsibility, and the meaning of an "
                              "education on a" + "\nuniversity campus.",
                              "John Singleton",
                              "Columbia Pictures",
                              "https://upload.wikimedia.org/wikipedia/en/2/26/Higher_Learning_%28movie%29.jpg",  # noqa
                              "https://www.youtube.com/watch?v=_4KVCVX1MrQ")

hotel_transylvania_2 = media.Movie("Hotel Transylvania 2", "1h 29m ",
                                   True, False,  # noqa
                                   "Dracula and his friends try to bring out "
                                   "the monster in his half human "
                                   "\nhalf vampire grandson in order to keep "
                                   "Mavis from leaving the hotel.",
                                   "Genndy Tartakovsky",
                                   "Columbia Pictures",
                                   "https://upload.wikimedia.org/wikipedia/en/5/5d/Hotel_Transylvania_2_poster.jpg",  # noqa
                                   "https://www.youtube.com/watch?v=T3nqmGgnJe8")  # noqa

lion_king = media.Movie("The Lion King", "1h 29m ", True, False,
                        "Lion cub and future king Simba searches for his "
                        "identity \nHis eagerness to please others and "
                        "penchant for testing his \nboundaries sometimes gets "
                        "him into trouble.", "Roger Allers and Rob Minkoff",
                        "Walt Disney Pictures",  # noqa
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

cinderella = media.Movie("Cinderella", "1h 28m ", True, False,
                         "Updated version of the classic Rodgers and "
                         "Hammerstein musical \nof the classic fairy-tale, "
                         "with an all-star, multi-racial cast.",
                         "Robert Iscove", "BrownHouse Productions",
                         "https://upload.wikimedia.org/wikipedia/en/f/f8/Cind_1997.jpg",  # noqa
                         "https://www.youtube.com/watch?v=EOKDuFW6XFo")

kill_bill = media.Movie("Kill Bill: Vol. 1", "1h 51m", True, False,
                        "The Bride wakens from a four-year coma. The child "
                        "she carried in her womb is gone. Now she \nmust "
                        "wreak vengeance on the team of assassins who "
                        "betrayed her.", "Quentin Tarantino", "A Band Apart",
                        "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",  # noqa
                        "https://www.youtube.com/watch?v=ot6C1ZKyiME")

color_purple = media.Movie("The Color Purple", "2h 34m", True, False,
                           "A black Southern woman struggles to find her "
                           "identity after suffering abuse from her \nfather "
                           "and others over four decades.", "Steven Spielberg",
                           "Warner Brothers",  # noqa
                           "https://upload.wikimedia.org/wikipedia/en/b/be/The_Color_Purple_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=d83NnlL83mc")

nightmare = media.Movie("The Nightmare Before Christmas", "1h 16m", True, False,  # noqa
                        "Jack Skellington, king of Halloween Town, discovers"
                        " Christmas Town, but doesn't quite \nunderstand "
                        "the concept.", "Henry Selick", "Touchstone Pictures",
                        "https://upload.wikimedia.org/wikipedia/en/9/9a/The_nightmare_before_christmas_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=wr6N_hZyBCk")

scrubs = media.Show("Scrubs", "Season 3", False, True, "22 Episodes ",
                    "In the unreal world of Sacred Heart Hospital, Dr. "
                    "John 'JD' Dorian learns \nthe ways of medicine, "
                    "friendship and life.", "ABC",  # noqa
                    "https://upload.wikimedia.org/wikipedia/en/4/45/Scrubs-s3-dvd.jpg",  # noqa
                    "https://www.youtube.com/watch?v=do9jR8Guz_E")

ahs_coven = media.Show("American Horror Story: Coven", "Season 3", False, True,
                       "13 Episodes ", "After discovering her unique bloodline"
                       ", a young girl is whisked \naway to a special academy"
                       " for girls who share the same lineage.", "FX",  # noqa
                       "https://upload.wikimedia.org/wikipedia/en/b/b2/American_Horror_Story_Season_3.jpg",  # noqa
                       "https://www.youtube.com/watch?v=NQRPiNRGoF8")

ahs_murder_house = media.Show("American Horror Story: Murder House", "Season 1",  # noqa
                              False, True, "12 Episodes ", "Therapist Ben"
                              " Harmon, his wife, Vivien, and their \ndaughter"
                              ", Violet, move across the country to Los"
                              "\nAngeles to escape their troubled past.",
                              "FX", "https://upload.wikimedia.org/wikipedia/en/e/eb/American_Horror_Story_Season_1.jpg",  # noqa
                              "https://www.youtube.com/watch?v=-9KZr2Vn7CQ")

will_grace = media.Show("Will & Grace", "Season 6", False, True, "24 Episodes ",  # noqa
                        "Will and Grace live together in an apartment in "
                        "New York. He's a gay lawyer, \nshe's a straight"
                        " interior designer.", "NBC",
                        "https://upload.wikimedia.org/wikipedia/en/0/01/Will_%26_Grace_Season_6.jpg",  # noqa
                        "https://www.youtube.com/watch?v=PbmZ39kEwGM")

oz = media.Show("Oz", "Season 2", False, True, "8 Episodes ",
                "In the aftermath of the riot that"
                "\nkilled six inmates and two officers,"
                "\nOz is locked down, and Emerald City prisoners"
                "\nare sent either to solitary or gen pop. A special"
                "\ncommittee is appointed to investigate the riot.",
                "HBO", "https://upload.wikimedia.org/wikipedia/en/9/9d/Ozposter.jpg",  # noqa
                "https://www.youtube.com/watch?v=F00xQE1DdXo")

desperate_housewives = media.Show("Desperate Housewives", "Season 8", False,
                                  True, "24 Episodes ",  # noqa
                                  "Secrets and truths unfold through the lives"
                                  " of female friends \nin one suburban"
                                  " neighborhood, after the mysterious suicide"
                                  " of a neighbor.", "ABC",  # noqa
                                  "https://upload.wikimedia.org/wikipedia/en/4/4a/DHWS8Promo.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=GVBCqGtkvvA")  # noqa

boondocks = media.Show("The Boondocks", "Season 2", False, True, "15 Episodes",
                       "Huey and Riley move away from the city and out to the"
                       " suburbs with their irascible \ngrandfather.",  # noqa
                       "Adult Swim",  # noqa
                       "https://upload.wikimedia.org/wikipedia/en/f/f6/Boondocks_season_2_DVD.png",  # noqa
                       "https://www.youtube.com/watch?v=FTMHx6JuQDw")

simpsons = media.Show("The Simpsons", "Season 17", False, True, "22 Episodes",
                      "The satiric adventures of a working-class family in the"
                      " misfit city of Springfield.", "Fox",
                      "https://upload.wikimedia.org/wikipedia/en/c/cf/The_Simpsons_-_The_17th_Season.jpg",  # noqa
                      "https://www.youtube.com/watch?v=R9fmstvhzog")

family_guy = media.Show("Family Guy", "Season 14", False, True, "20 Episodes",
                        "In a wacky Rhode Island town, a dysfunctional family"
                        " strive to cope with everyday life \nas they are"
                        " thrown from one crazy scenario to another.", "Fox",
                        "https://upload.wikimedia.org/wikipedia/en/4/49/Family_Guy_%28season_14%29.jpg",  # noqa
                        "https://www.youtube.com/watch?v=rB_VUVUA_QI")

# Put video objects in an array
videos = [godfather, fresh, scrubs, oz, cinderella, will_grace,  # noqa
          desperate_housewives, lion_king, hotel_transylvania_2,  # noqa
          higher_learning, ahs_coven, ahs_murder_house, boondocks,  # noqa
          kill_bill, color_purple, simpsons, family_guy, nightmare]

# put videos array in method that renders webpage
fresh_tomatoes.open_videos_page(videos)  # noqa
