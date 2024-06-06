-- createdb.ddl - prepares the initial database environment. Modify this if you need.
-- Copyright (C) 2024 Yasuhiro Hayashi

ALTER USER postgres WITH PASSWORD 'c4cf7065b034787b2061088190bf737e'; 

DROP TABLE IF EXISTS users;
CREATE TABLE users ( 
    id SERIAL PRIMARY KEY, 
    username CHARACTER VARYING(64), 
    password CHARACTER VARYING(128) 
); 

DROP TABLE IF EXISTS spots;
CREATE TABLE spots ( 
    id SERIAL PRIMARY KEY, 
    user_id INTEGER NOT NULL, 
    area CHARACTER VARYING(128), 
    cityname CHARACTER VARYING(128), 
    spotname CHARACTER VARYING(128), 
    datetime TIMESTAMP WITH TIME ZONE,
    latitude DOUBLE PRECISION, 
    longitude DOUBLE PRECISION, 
    url CHARACTER VARYING(128), 
    picture CHARACTER VARYING(1024), 
    history_culture INTEGER, 
    food_product INTEGER, 
    nature INTEGER, 
    views INTEGER, 
    experience INTEGER, 
    opentime TIME WITH TIME ZONE,
    closetime TIME WITH TIME ZONE
);

ALTER TABLE spots ADD CONSTRAINT spots_user_id_fkey FOREIGN KEY (user_id) REFERENCES users (id); 

INSERT INTO users (username, password) VALUES 
('admin', 'password'), 
('user', 'password')
; 

INSERT INTO spots (user_id, area, cityname, spotname, datetime, latitude, longitude, url, picture, history_culture, food_product, nature, views, experience, opentime, closetime) VALUES 
( 1, 'newyork', 'New York', 'Statue of Liberty', '2020-01-23', '40.6896', '-74.0453', 'https://www.nps.gov/stli/', 'https://upload.wikimedia.org/wikipedia/commons/d/dd/Lady_Liberty_under_a_blue_sky_%28cropped%29.jpg', 1, 0, 0, 1, 1, '10:00:00', '17:00:00' ), 
( 1, 'newyork', 'New York', 'Central Park', '2020-01-23', '40.7826', '-73.9653', 'https://www.planetware.com/new-york-city/new-york-central-park-us-ny-central.htm', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Global_Citizen_Festival_Central_Park_New_York_City_from_NYonAir_%2815351915006%29.jpg/600px-Global_Citizen_Festival_Central_Park_New_York_City_from_NYonAir_%2815351915006%29.jpg', 1, 0, 1, 1, 1, '00:00:00', '00:00:00' ), 
( 1, 'newyork', 'New York', 'Rockefeller Center', '2020-01-24', '40.75926', '-73.97995', 'https://www.rockefellercenter.com', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/GE_Building_by_David_Shankbone.JPG/500px-GE_Building_by_David_Shankbone.JPG', 1, 0, 0, 1, 0, '10:00:00', '20:00:00' ), 
( 1, 'newyork', 'New York', 'Metropolitan Museum of Art', '2020-01-24', '40.77937', '-73.96337', 'https://www.metmuseum.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Metropolitan_Museum_of_Art_%28The_Met%29_-_Central_Park%2C_NYC.jpg/480px-Metropolitan_Museum_of_Art_%28The_Met%29_-_Central_Park%2C_NYC.jpg', 1, 0, 0, 0, 1, '10:00:00', '17:00:00' ), 
( 1, 'newyork', 'New York', 'Broadway and the Theater District', '2020-01-24', '40.76146', '-73.98406999999997', 'http://www.broadway.com', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Broadway_Theaters_45th_Street_Night.jpg/250px-Broadway_Theaters_45th_Street_Night.jpg', 1, 0, 0, 1, 1, '10:00:00', '22:00:00' ), 
( 1, 'newyork', 'New York', 'Empire State Building', '2020-01-24', '40.74844', '-73.98568', 'http://www.esbnyc.com', 'https://upload.wikimedia.org/wikipedia/commons/c/c7/Empire_State_Building_from_the_Top_of_the_Rock.jpg', 0, 0, 0, 1, 1, '10:00:00', '20:00:00' ), 
( 1, 'newyork', 'New York', '9/11 Memorial and Museum', '2020-03-10', '40.7114', '-74.01264', 'http://www.911memorial.org', 'https://upload.wikimedia.org/wikipedia/commons/f/fc/9-11_Memorial_and_Museum_%2828815276064%29.jpg', 1, 0, 0, 1, 1, '10:00:00', '17:00:00' ), 
( 1, 'newyork', 'New York', 'High Line', '2020-03-14', '40.7474', '-74.0048', 'https://www.thehighline.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/AHigh_Line_Park%2C_Section_1a.jpg/580px-AHigh_Line_Park%2C_Section_1a.jpg', 0, 0, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'newyork', 'New York', 'Times Square', '2020-04-23', '40.7560578', '-73.9862997', 'http://www.timessquarenyc.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/600px-New_york_times_square-terabass.jpg', 1, 0, 0, 0, 1, '10:00:00', '22:00:00' ), 
( 1, 'newyork', 'New York', 'Brooklyn Bridge', '2020-04-29', '40.7052', '-73.9958', 'https://www.nycgo.com/articles/guide-to-the-brooklyn-bridge', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Brooklyn_Bridge_Manhattan.jpg/500px-Brooklyn_Bridge_Manhattan.jpg', 1, 0, 0, 1, 0, '00:00:00', '00:00:00' ), 
( 1, 'newyork', 'New York', 'Fifth Avenue', '2020-06-02', '40.7537', '-73.98196', 'https://visit5thavenue.com', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Fifth_Avenue.jpg/640px-Fifth_Avenue.jpg', 0, 0, 0, 0, 0, '00:00:00', '00:00:00' ), 
( 1, 'newyork', 'New York', 'Grand Central Terminal', '2020-08-09', '40.7528064', '-73.9771792', 'https://www.grandcentralterminal.com', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Image-Grand_central_Station_Outside_Night_2.jpg/2560px-Image-Grand_central_Station_Outside_Night_2.jpg', 0, 0, 0, 0, 0, '05:00:00', '23:00:00' ), 
( 1, 'newyork', 'New York', 'One World Observatory', '2020-09-27', '40.712949', '-74.01304379999998', 'https://www.oneworldobservatory.com/en-US', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/One_World_Observatory_View.jpg/900px-One_World_Observatory_View.jpg', 0, 0, 0, 1, 0, '10:00:00', '20:00:00' ), 
( 1, 'newyork', 'New York', 'The Frick Collection', '2020-10-04', '40.77125', '-73.9671', 'https://www.frick.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Frickmusjeh.JPG/580px-Frickmusjeh.JPG', 0, 1, 0, 0, 0, '10:00:00', '20:00:00' ), 
( 1, 'newyork', 'New York', 'New York Public Library', '2020-10-04', '40.75334', '-73.98216', 'https://www.nypl.org/locations/schwarzman', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/New_York_Public_Library_-_Main_Branch_%2851396225599%29.jpg/460px-New_York_Public_Library_-_Main_Branch_%2851396225599%29.jpg', 1, 0, 0, 0, 0, '10:00:00', '17:00:00' ), 
( 1, 'newyork', 'New York', 'Wall Street', '2020-11-10', '40.70763', '-74.01148', 'https://freetoursbyfoot.com/things-to-do-and-see-on-wall-street/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Photos_NewYork1_032.jpg/800px-Photos_NewYork1_032.jpg', 1, 0, 0, 0, 0, '00:00:00', '00:00:00' ), 
( 1, 'newyork', 'New York', 'Radio City Music Hall', '2020-11-21', '40.759809999999995', '-73.97928', 'https://www.msg.com/radio-city-music-hall', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Radio_City_Music_Hall_%2851395756913%29.jpg/600px-Radio_City_Music_Hall_%2851395756913%29.jpg', 1, 0, 0, 0, 0, '10:00:00', '20:00:00' ), 
( 1, 'newyork', 'New York', 'St. Patrick''s Cathedral', '2020-11-22', '40.75856', '-73.97636999999997', 'https://saintpatrickscathedral.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/At_New_York%2C_USA_2017_119.jpg/440px-At_New_York%2C_USA_2017_119.jpg', 1, 0, 0, 0, 1, '10:00:00', '17:00:00' ), 
( 1, 'newyork', 'New York', 'Carnegie Hall', '2020-12-21', '40.76503', '-73.97989', 'https://www.carnegiehall.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Carnegie_Hall_-_Full_%2848155558466%29.jpg/500px-Carnegie_Hall_-_Full_%2848155558466%29.jpg', 1, 0, 0, 0, 1, '10:00:00', '17:00:00' ), 
( 1, 'newyork', 'New York', 'Bryant Park', '2020-12-27', '40.75376', '-73.98356', 'https://bryantpark.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/New-York_-_Bryant_Park.jpg/650px-New-York_-_Bryant_Park.jpg', 0, 0, 1, 0, 1, '00:00:00', '00:00:00' ), 
( 1, 'london', 'London', 'Buckingham Palace and the Changing of the Guard', '2020-01-04', '51.500809999999994', '-0.14299', 'https://www.rct.uk/visit/the-state-rooms-buckingham-palace', 'https://www.householddivision.org.uk/uploads/main_photos/photo_29.jpg', 1, 0, 1, 1, 1, '10:00:00', '17:00:00' ), 
( 1, 'london', 'London', 'The Tower of London and Tower Bridge', '2020-01-23', '51.50807', '-0.07619', 'https://www.planetware.com/london/tower-of-london-eng-l-tl.htm', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Tower_Bridge_London_Feb_2006.jpg/600px-Tower_Bridge_London_Feb_2006.jpg', 1, 0, 0, 1, 1, '10:00:00', '20:00:00' ), 
( 1, 'london', 'London', 'The British Museum', '2020-02-03', '51.51942', '-0.127', 'https://www.britishmuseum.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/British_Museum_%28aerial%29.jpg/500px-British_Museum_%28aerial%29.jpg', 1, 0, 0, 0, 1, '10:00:00', '18:00:00' ), 
( 1, 'london', 'London', 'Big Ben and Parliament', '2020-03-03', '51.5007', '-0.12458', 'https://www.parliament.uk/bigben/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Parliament_and_Big_Ben_%28Unsplash%29.jpg/1599px-Parliament_and_Big_Ben_%28Unsplash%29.jpg', 1, 0, 0, 1, 1, '10:00:00', '17:00:00' ), 
( 1, 'london', 'London', 'National Gallery', '2020-04-15', '51.50889', '-0.12839', 'https://www.nationalgallery.org.uk', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Galería_Nacional%2C_Londres%2C_Inglaterra%2C_2014-08-07%2C_DD_035.JPG/500px-Galería_Nacional%2C_Londres%2C_Inglaterra%2C_2014-08-07%2C_DD_035.JPG', 1, 0, 0, 0, 1, '10:00:00', '17:00:00' ), 
( 1, 'london', 'London', 'The Victoria and Albert Museum', '2020-04-25', '51.49674', '-0.1716099999999999', 'https://www.vam.ac.uk', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Victoria_%26_Albert_Museum_Entrance%2C_London%2C_UK_-_Diliff.jpg/500px-Victoria_%26_Albert_Museum_Entrance%2C_London%2C_UK_-_Diliff.jpg', 1, 0, 0, 0, 1, '10:00:00', '17:00:00' ), 
( 1, 'london', 'London', 'Piccadilly Circus and Trafalgar Square', '2020-05-23', '51.50979', '-0.13455', 'https://www.planetware.com/london/trafalgar-square-eng-l-ts.htm', 'https://media.tacdn.com/media/attractions-splice-spp-674x446/09/27/f5/de.jpg', 1, 1, 0, 0, 1, '00:00:00', '00:00:00' ), 
( 1, 'london', 'London', 'The Shard', '2020-06-11', '51.50435', '-0.08645', 'https://www.the-shard.com', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/The_Shard_from_the_Sky_Garden_2015.jpg/500px-The_Shard_from_the_Sky_Garden_2015.jpg', 0, 0, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'london', 'London', 'The Two Tates: Tate Britain and Tate Modern', '2020-06-21', '51.49109', '-0.12785', 'https://www.tate.org.uk', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Tate_Modern_-_Bankside_Power_Station.jpg/500px-Tate_Modern_-_Bankside_Power_Station.jpg', 0, 0, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'london', 'London', 'Westminster Abbey', '2020-07-25', '51.49935', '-0.1274', 'https://www.westminster-abbey.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Westminster_Abbey_St_Peter.jpg/440px-Westminster_Abbey_St_Peter.jpg', 1, 0, 0, 0, 0, '10:00:00', '17:00:00' ), 
( 1, 'london', 'London', 'Churchill''s War Rooms', '2020-08-03', '51.5022', '-0.12928', 'https://www.iwm.org.uk/visits/churchill-war-rooms', 'https://a.cdn-hotels.com/gdcs/production72/d1430/d7ff752d-08ee-4245-83ab-942d30fbdff5.jpg?impolicy=fcrop&w=1600&h=1066&q=medium', 1, 0, 0, 0, 0, '10:00:00', '17:00:00' ), 
( 1, 'london', 'London', 'Natural History Museum', '2020-08-10', '51.49649', '-0.17602', 'https://www.nhm.ac.uk', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Natural_History_Museum_London_Jan_2006.jpg/500px-Natural_History_Museum_London_Jan_2006.jpg', 1, 0, 0, 0, 1, '10:00:00', '18:00:00' ), 
( 1, 'london', 'London', 'Hyde Park', '2020-08-20', '51.5074', '-0.1621', 'https://www.planetware.com/london/hyde-park-eng-l-hy.htm', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Hyde_Park_London_from_the_air.jpg/600px-Hyde_Park_London_from_the_air.jpg', 0, 0, 1, 1, 1, '00:00:00', '00:00:00' ), 
( 1, 'london', 'London', 'St. Paul''s Cathedral', '2020-08-31', '51.51379', '-0.09845', 'https://www.stpauls.co.uk', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/St_Pauls_aerial_%28cropped%29.jpg/440px-St_Pauls_aerial_%28cropped%29.jpg', 1, 0, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'london', 'London', 'Covent Garden', '2020-09-01', '51.51175', '-0.12268', 'https://www.coventgarden.london', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Covent_Garden_Interior_May_2006_crop.jpg/600px-Covent_Garden_Interior_May_2006_crop.jpg', 0, 0, 1, 1, 1, '00:00:00', '00:00:00' ), 
( 1, 'london', 'London', 'The London Eye', '2020-09-09', '51.50328', '-0.1197', 'https://www.londoneye.com', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/London-Eye-2009.JPG/500px-London-Eye-2009.JPG', 0, 0, 0, 1, 0, '10:00:00', '20:00:00' ), 
( 1, 'london', 'London', 'Hampton Court Palace', '2020-09-10', '51.40369000000001', '-0.33769', 'https://www.hrp.org.uk/hampton-court-palace/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Great_Gate%2C_Hampton_Court_Palace.jpg/500px-Great_Gate%2C_Hampton_Court_Palace.jpg', 1, 0, 0, 1, 0, '10:00:00', '20:00:00' ), 
( 1, 'london', 'London', 'Greenwich and Docklands', '2020-09-27', '51.4821', '-0.0046', 'https://www.visitgreenwich.org.uk/docklands-and-beyond/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Canary_Wharf_from_Greenwich_riverside_2022-03-18.jpg/1600px-Canary_Wharf_from_Greenwich_riverside_2022-03-18.jpg', 0, 0, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'london', 'London', 'Kew Gardens', '2020-12-24', '51.4771', '-0.2849', 'https://www.kew.org', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Kew_Gardens_Palm_House%2C_London_-_July_2009.jpg/600px-Kew_Gardens_Palm_House%2C_London_-_July_2009.jpg', 0, 0, 1, 1, 1, '10:00:00', '20:00:00' ), 
( 1, 'london', 'London', 'The Harry Potter Shop at Platform 9¾', '2020-12-25', '51.532', '-0.123', 'https://www.visitlondon.com/things-to-do/sightseeing/london-attraction/harry-potters-london', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/KingsCrossOutside.JPG/530px-KingsCrossOutside.JPG', 0, 1, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Asakusa - Sensoji Temple', '2020-02-27', '35.71113', '139.79637', 'https://www.senso-ji.jp', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Cloudy_Sensō-ji.jpg/520px-Cloudy_Sensō-ji.jpg', 1, 1, 0, 0, 1, '05:00:00', '17:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'The Outer Market at Tsukiji Fish Market', '2020-03-07', '35.66540999999999', '139.7706', 'https://www.tsukiji.or.jp/english/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Tsukiji_Outer_Market_-08.jpg/600px-Tsukiji_Outer_Market_-08.jpg', 0, 1, 0, 0, 0, '10:00:00', '24:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Ueno - Ameyoko', '2020-03-09', '35.71005', '139.77454', 'http://www.ameyoko.net', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Ameyoko_Ueno_Tokyo_Japan.jpg/1600px-Ameyoko_Ueno_Tokyo_Japan.jpg', 0, 1, 0, 0, 0, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Shibuya - Scramble Crossing', '2020-03-18', '35.65948', '139.70054', 'https://matcha-jp.com/en/1141', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/2018_Shibuya_Crossing.jpg/500px-2018_Shibuya_Crossing.jpg', 0, 1, 0, 0, 0, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Oshiage - Tokyo Skytree', '2020-04-10', '35.71006', '139.81071', 'https://www.tokyo-skytree.jp/en/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Tokyo_Skytree_2014_Ⅲ.jpg/290px-Tokyo_Skytree_2014_Ⅲ.jpg', 0, 1, 0, 1, 0, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Ginza - Kabukiza Theater', '2020-04-21', '35.66967', '139.76806000000002', 'https://www.kabukiweb.net/theatres/kabukiza/information/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/2019_Kabuki-za.jpg/600px-2019_Kabuki-za.jpg', 0, 0, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Odaiba - Oedo Onsen Monogatari', '2020-07-01', '35.61552000000001', '139.7776', 'https://daiba.ooedoonsen.jp/en/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Oedo_Onsen_Monogatari.JPG/600px-Oedo_Onsen_Monogatari.JPG', 0, 1, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Mitaka - Ghibli Museum', '2020-07-04', '35.69623', '139.57043000000002', 'Ghibli Museum', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Ghibli_Museum%2C_Mitaka_-_panoramio.jpg/440px-Ghibli_Museum%2C_Mitaka_-_panoramio.jpg', 0, 1, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Roppongi - Roppongi Hills', '2020-08-29', '35.6599', '139.72975', 'https://www.roppongihills.com/en/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Roppongi_Hills_2013-12-01.jpg/560px-Roppongi_Hills_2013-12-01.jpg', 0, 1, 0, 0, 0, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Harajuku - Meiji Shrine', '2020-09-10', '35.6748', '139.6996', 'https://www.meijijingu.or.jp/en/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Meiji_Jingu_2023-3.jpg/1200px-Meiji_Jingu_2023-3.jpg', 0, 1, 0, 0, 0, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Hamarikyu Gardens', '2020-10-29', '35.6601', '139.7638', 'https://www.tokyo-park.or.jp/park/format/index028.html#googtrans(en)', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Hamarikyu_Garden_as_seen_from_Shiodome.jpg/500px-Hamarikyu_Garden_as_seen_from_Shiodome.jpg', 1, 0, 1, 1, 0, '10:00:00', '17:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Edo-Tokyo Open Air Architectural Museum', '2020-10-30', '35.71618', '139.51273', 'https://www.tatemonoen.jp/english/', 'https://upload.wikimedia.org/wikipedia/commons/1/14/Edo-Tokyo_Open_Air_Architectural_Museum_PB252276.jpg', 0, 0, 0, 0, 1, '10:00:00', '17:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Tokyo Tower', '2020-11-05', '35.65858', '139.74544', 'https://www.tokyotower.co.jp/en/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Tokyo_Tower_2023.jpg/540px-Tokyo_Tower_2023.jpg', 1, 1, 0, 1, 0, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Akihabara - Anime attractions', '2020-11-05', '35.702', '139.7742', 'https://www.gotokyo.org/en/destinations/central-tokyo/akihabara/index.html', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Akihabara.png/500px-Akihabara.png', 0, 1, 0, 0, 1, '10:00:00', '24:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Ryogoku Kokugikan - The Professional Sumo', '2020-11-11', '35.69688', '139.79345', 'http://www.sumo.or.jp/En/', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Ryogoku_Kokugikan_Tsuriyane_05212006.jpg', 1, 0, 1, 0, 0, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Edo-Tokyo, Museum', '2020-11-12', '35.69639', '139.79562', 'https://www.edo-tokyo-museum.or.jp/en/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Edo-Tokyo_Museum.jpg/600px-Edo-Tokyo_Museum.jpg', 1, 0, 0, 0, 1, '10:00:00', '17:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Tokyo Dome City Attractions', '2020-11-15', '35.7044', '139.75419', 'https://www.tokyo-dome.co.jp/en/tourists/attractions/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Tokyo_Dome_%2852480559907%29.jpg/500px-Tokyo_Dome_%2852480559907%29.jpg', 0, 0, 0, 0, 1, '10:00:00', '20:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Tokyo Imperial Palace', '2020-11-25', '35.6814', '139.7567', 'https://www.japan-guide.com/e/e3017.html', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Seimon_Ishibashi.JPG/500px-Seimon_Ishibashi.JPG', 1, 0, 1, 1, 0, '00:00:00', '00:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Shinjuku Gyoen National Garden', '2020-12-08', '35.6851', '139.7095', 'https://www.gotokyo.org/en/spot/75/index.html', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Shinjuku_Gyoen_National_Garden_-_sakura_3.JPG/600px-Shinjuku_Gyoen_National_Garden_-_sakura_3.JPG', 1, 0, 1, 1, 0, '10:00:00', '17:00:00' ), 
( 1, 'tokyo', 'Tokyo', 'Tokyo Disney Resort', '2020-12-25', '35.6312', '139.8808', 'https://www.tokyodisneyresort.jp/en/index.html', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/A8_Tokyo_Disneyland.jpg/440px-A8_Tokyo_Disneyland.jpg', 0, 1, 0, 0, 1, '08:00:00', '22:00:00' ) 
;

CREATE OR REPLACE FUNCTION gis_distance(p1 POINT, p2 POINT) 
RETURNS TABLE (result DOUBLE PRECISION) 
AS $$
BEGIN
    RETURN QUERY 
    SELECT 2 * r * ASIN( d / 2 / r )
    FROM (
        SELECT SQRT((x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2) AS d, r 
        FROM ( 
            SELECT
                c.r, 
                c.r * COS(PI() * l1.lat/180) * COS(PI() * l1.lng/180) AS x1, 
                c.r * COS(PI() * l1.lat/180) * SIN(PI() * l1.lng/180) AS y1, 
                c.r * SIN(PI() * l1.lat/180)                          AS z1, 
                c.r * COS(PI() * l2.lat/180) * COS(PI() * l2.lng/180) AS x2, 
                c.r * COS(PI() * l2.lat/180) * SIN(PI() * l2.lng/180) AS y2, 
                c.r * SIN(PI() * l2.lat/180)                          AS z2 
            FROM 
                (SELECT $1[0] AS lat, $1[1] AS lng) AS l1, 
                (SELECT $2[0] AS lat, $2[1] AS lng) AS l2, 
                (SELECT 6378.137 AS r) AS c 
        ) AS trig 
    ) AS sq; 
END;
$$ LANGUAGE plpgsql;
