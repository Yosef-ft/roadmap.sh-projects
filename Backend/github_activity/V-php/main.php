<?php

function getGitUserActivity($username){
    try{
      $url = "https://api.github.com/users/{$username}/events";
      $ch = curl_init($url);  
  
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, ["User-Agent: PHP"]);
      curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
  
      $response = curl_exec($ch);
  
      if ($response == false){
        throw new Exception('Network response was not ok', curl_error($ch));
      }
  
      $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      curl_close($ch);
  
      if ($http_code !== 200){
        throw new Exception("Http faild with status code: $http_code");
      }
  
      $data = json_decode($response);
      if($data == null){
        throw new Exception("Error parsing json");
      }
  
      return $data;
    }catch(Exception $error){
      error_log('Problem fetching activity' . $error->getMessage());
      return [];
    }catch(Throwable $error){
      error_log('An unknown error occured' . $error->getMessage());
      return [];
    }
}


if(php_sapi_name() === 'cli'){
  $username = isset($argv[1]) ? $argv[1] : null;

  if(!$username){
    echo "Please provide gihub username";
  }else{
    $response = getGitUserActivity($username);
    foreach ($response as $gitEvent) {
        echo "{$gitEvent->type} :: {$gitEvent->repo->name}\n";
    }    
  }
}