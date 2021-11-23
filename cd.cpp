





instagram.com
   $instagram = \InstagramScraper\Instagram::withCredentials(new \GuzzleHttp\Client(), 'username', 'password', new Psr16Adapter('Files'));
$instagram->login();

$media = $instagram->getMediaByUrl('https://www.instagram.com/p/BQ0lhTeAYo5');
echo "Media info:\n";
printMediaInfo($media);
$instagram = \InstagramScraper\Instagram::withCredentials(new \GuzzleHttp\Client(), 'username', 'password', new Psr16Adapter('Files'));
$instagram->login();

$media = $instagram->getMediaByUrl('https://www.instagram.com/p/BHaRdodBouH');
echo "Media info:\n";
echo "Id: {$media->getId()}\n";
echo "Shortcode: {$media->getShortCode()}\n";










































































































google.com
ext-align:right;user-select:none">238
ext-align:right;user-select:none">239def sentiment_analysis(text, language_of_text, logger):
ext-align:right;user-select:none">240    """
ext-align:right;user-select:none">241    Perform a detailed multilingual sentiment analysis of texts from
ext-align:right;user-select:none">242    different sources
ext-align:right;user-select:none">243    Available responses:
ext-align:right;user-select:none">244        https://github.com/MeaningCloud/meaningcloud-python/blob/master
ext-align:right;user-select:none">245
ext-align:right;user-select:none">59                heavy_post_ids.append(postobj)
ext-align:right;user-select:none">60            else:
ext-align:right;user-select:none">61                normal_post_ids.append(postobj)
ext-align:right;user-select:none">62        except Exception as err:
ext-align:right;user-select:none">63            logger.error(
ext-align:right;user-select:none">64                "Failed with Error {}, please upgrade your instapy".format(err)
ext-align:right;user-select:none">65            )
ext-align:right;user-select:none">66
 else:
            logger.error(r.text)
            return []
    except Exception as err:
        logger.error("Could not get postids from pod {} - {}".format(topic, err))
        return []
ext-align:right;user-select:none">39        else:
ext-align:right;user-select:none">40            logger.error(r.text)
ext-align:right;user-select:none">41            return []
ext-align:right;user-select:none">42    except Exception as err:
ext-align:right;user-select:none">43        logger.error("Could not get postids from pod {} - {}".format(topic, err))
ext-align:right;user-select:none">44        return []
ext-align:right;user-select:none">45
ext-align:right;user-select:none">46
ext-align:right;user-select:none">241                + "   - /stop (force stop the bot)\n",
ext-align:right;user-select:none">242            )
ext-align:right;user-select:none">243
ext-align:right;user-select:none">244    def _check_authorized(self, update, context):
ext-align:right;user-select:none">245        """
ext-align:right;user-select:none">246        check if a user is authorized to use this bot
ext-align:right;user-select:none">247        :param update:
ext-align:right;user-select:none">248


