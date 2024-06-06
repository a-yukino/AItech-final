import PIL.ExifTags as ExifTags

def extract_datetime(im):
    try:
        im_exif = im._getexif()
        exif = {
            ExifTags.TAGS[MyKey]: MyValue
            for MyKey, MyValue in im_exif.items()
            if MyKey in ExifTags.TAGS
        }
        if 'DateTimeOriginal' in exif:
            date_tags = str(exif['DateTimeOriginal'])
            return date_tags.replace(':', '/', 2)
    except AttributeError:
        return {}

def extract_geocode(im):
    try:
        im_exif = im._getexif()
        exif = {
            ExifTags.TAGS[MyKey]: MyValue
            for MyKey, MyValue in im_exif.items()
            if MyKey in ExifTags.TAGS
        }
        if 'GPSInfo' in exif:
            gps_tags = exif['GPSInfo']
            gps = {
                ExifTags.GPSTAGS.get(t, t): gps_tags[t]
                for t in gps_tags
            }

            is_lat = 'GPSLatitude' in gps
            is_lat_ref = 'GPSLatitudeRef' in gps
            is_lon = 'GPSLongitude' in gps
            is_lon_ref = 'GPSLongitudeRef' in gps

            if is_lat and is_lat_ref and is_lon and is_lon_ref:
                lat = gps['GPSLatitude']
                lat_ref = gps['GPSLatitudeRef']
                lon = gps['GPSLongitude']
                lon_ref = gps['GPSLongitudeRef']

                # 北緯の場合プラス、南緯の場合マイナスを設定
                if lat_ref == 'N':
                    lat_sign = 1.0
                elif lat_ref == 'S':
                    lat_sign = -1.0

                # 東経の場合プラス、西経の場合マイナスを設定
                if lon_ref == 'E':
                    lon_sign = 1.0
                elif lon_ref == 'W':
                    lon_sign = -1.0

                lat_ang0 = lat_sign * lat[0] + lat[1] / 60 + lat[2] / 3600
                lon_ang0 = lon_sign * lon[0] + lon[1] / 60 + lon[2] / 3600

                return str(lat_ang0), str(lon_ang0)
    except AttributeError:
        return {}
