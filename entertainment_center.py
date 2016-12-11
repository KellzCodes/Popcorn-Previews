import media
import fresh_tomatoes

"""
Creates various instances of the classes Movie and Show.
"""

godfather = media.Movie("The Godfather", "2h 58m ", True, False,
                        "The aging patriarch of a crime dynasty" +
                        "\ntransfers control of his empire to his" +
                        "\nreluctant son.", "Francis Ford Coppola", "Paramount Pictures",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

fresh = media.Movie("Fresh", "1h 55m ", True, False,
                    "In a world where criminals make the rules, a 12 year old " +
                    "\nboy is out to beat them at their own game.", "Boaz Yakin", "Miramax",
                    "https://upload.wikimedia.org/wikipedia/en/c/cd/Fresh_movie_90s.jpg",
                    "https://www.youtube.com/watch?v=y7QvSl4C4hE")

higher_learning = media.Movie("Higher Learning", "2h 8m ", True, False,
                              "People, from all different walks of life, encounter racial tension, " +
                              "\nrape, responsibility, and the meaning of an education on a " +
                              "\nuniversity campus.",
                              "John Singleton",
                              "Columbia Pictures",
                              "https://upload.wikimedia.org/wikipedia/en/2/26/Higher_Learning_%28movie%29.jpg",
                              "https://www.youtube.com/watch?v=_4KVCVX1MrQ")

hotel_transylvania_2 = media.Movie("Hotel Transylvania 2", "1h 29m ", True, False,
                                   "Dracula and his friends try to bring out the monster in his half human " +
                                   "\nhalf vampire grandson in order to keep Mavis from leaving the hotel.",
                                   "Genndy Tartakovsky",
                                   "Columbia Pictures",
                                   "https://upload.wikimedia.org/wikipedia/en/5/5d/Hotel_Transylvania_2_poster.jpg",
                                   "https://www.youtube.com/watch?v=T3nqmGgnJe8")

lion_king = media.Movie("The Lion King", "1h 29m ", True, False,
                        "Lion cub and future king Simba searches for his identity." +
                        "\nHis eagerness to please others and penchant for testing his" +
                        "\nboundaries sometimes gets him into trouble.",
                        "Roger Allers and Rob Minkoff",
                        "Walt Disney Pictures",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

cinderella = media.Movie("Cinderella", "1h 28m ", True, False,
                         "Updated version of the classic Rodgers and Hammerstein musical" +
                         "\nof the classic fairy-tale, with an all-star, multi-racial cast.",
                         "Robert Iscove",
                         "BrownHouse Productions",
                         "https://upload.wikimedia.org/wikipedia/en/f/f8/Cind_1997.jpg",
                         "https://www.youtube.com/watch?v=EOKDuFW6XFo")

scrubs = media.Show("Scrubs", "Season 3", False, True, "22 Episodes ",
                    "In the unreal world of Sacred Heart Hospital, Dr. John 'JD' Dorian learns" +
                    "\nthe ways of medicine, friendship and life.",
                    "ABC", "https://upload.wikimedia.org/wikipedia/en/4/45/Scrubs-s3-dvd.jpg",
                    "https://www.youtube.com/watch?v=do9jR8Guz_E")

ahs_coven = media.Show("American Horror Story: Coven", "Season 3", False, True, "13 Episodes ",
                       "After discovering her unique bloodline, a young girl is whisked" +
                       "\naway to a special academy for girls who share the same lineage.",
                       "FX", "https://upload.wikimedia.org/wikipedia/en/b/b2/American_Horror_Story_Season_3.jpg",
                       "https://www.youtube.com/watch?v=NQRPiNRGoF8")

ahs_murder_house = media.Show("American Horror Story: Murder House", "Season 1", False, True, "12 Episodes ",
                              "Therapist Ben Harmon, his wife, Vivien, and their" +
                              "\ndaughter, Violet, move across the country to Los" +
                              "\nAngeles to escape their troubled past.",
                              "FX", "https://upload.wikimedia.org/wikipedia/en/e/eb/American_Horror_Story_Season_1.jpg",
                              "https://www.youtube.com/watch?v=-9KZr2Vn7CQ")

will_grace = media.Show("Will & Grace", "Season 6", False, True, "24 Episodes ",
                        "Will and Grace live together in an apartment in New York. He's a gay lawyer," +
                        "\nshe's a straight interior designer.",
                        "NBC", "https://upload.wikimedia.org/wikipedia/en/0/01/Will_%26_Grace_Season_6.jpg",
                        "https://www.youtube.com/watch?v=PbmZ39kEwGM")

oz = media.Show("Oz", "Season 2", False, True, "8 Episodes ",
                "In the aftermath of the riot that" +
                "\nkilled six inmates and two officers," +
                "\nOz is locked down, and Emerald City prisoners" +
                "\nare sent either to solitary or gen pop. A special" +
                "\ncommittee is appointed to investigate the riot.",
                "HBO", "https://upload.wikimedia.org/wikipedia/en/b/b8/Oz_titlecard.png",
                "https://www.youtube.com/watch?v=F00xQE1DdXo")

desperate_housewives = media.Show("Desperate Housewives", "Season 8", False, True, "24 Episodes ",
                                  "Secrets and truths unfold through the lives of female friends" +
                                  "\nin one suburban neighborhood, after the mysterious suicide of a neighbor.",
                                  "ABC", "https://upload.wikimedia.org/wikipedia/en/4/4a/DHWS8Promo.jpg",
                                  "https://www.youtube.com/watch?v=GVBCqGtkvvA")

# Put video objects in an array
videos = [godfather, fresh, higher_learning, hotel_transylvania_2, lion_king, cinderella,
          scrubs, ahs_coven, ahs_murder_house, will_grace, oz, desperate_housewives]

fresh_tomatoes.open_videos_page(videos) # put videos array in method that renders webpage


