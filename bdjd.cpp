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
