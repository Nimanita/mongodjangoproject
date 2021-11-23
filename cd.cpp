 bbox = get_bounding_box(
                lat, lon, logger=self.logger, half_side_in_miles=radius
            )
            bbox_url = "{},{},{},{}&zoom={}".format(
                bbox["lon_min"],
                bbox["lat_min"],
                bbox["lon_max"],
      bbox["lat_max"],
                radius,
            )
            url = "https://apidisplaypurposes.com/local/?bbox={}".format(bbox_url)

            req = requests.get(url)
            data = json.loads(req.text)
        url = "https://apidisplaypurposes.com/local/?bbox={}".format(bbox_url)

            req = requests.get(url)
            data = json.loads(req.text)
            if int(data["count"]) == 0:
                self.logger.warning("Too few results for {} location".format(location))
