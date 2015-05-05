<?php
session_start();
require_once("twitteroauth/twitteroauth/twitteroauth.php"); //Path to twitteroauth library
 
$twitteruser = "aaaronlopez";
$notweets = 30;
$consumerkey = "IHO7c3kX9cPXeC5yymwkX7ySF";
$consumersecret = "5WxVESOsFbF87KviFjn8S1oROjHrfmOLNMKfH0gbMgNAAkwU69";
$accesstoken = "2241581574-oaHtX7XWAjk2Ljv7TAobCCry3l5sW9ZUrKqGuWf";
$accesstokensecret = "aDjl7gNSIGIKjwumv2XqGtJXIHsC5WepRwhHVCBG8UKqP";
 
function getConnectionWithAccessToken($cons_key, $cons_secret, $oauth_token, $oauth_token_secret) {
  $connection = new TwitterOAuth($cons_key, $cons_secret, $oauth_token, $oauth_token_secret);
  return $connection;
}
 
$connection = getConnectionWithAccessToken($consumerkey, $consumersecret, $accesstoken, $accesstokensecret);
 
$tweets = $connection->get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=".$twitteruser."&count=".$notweets);
 
echo json_encode($tweets);
?>