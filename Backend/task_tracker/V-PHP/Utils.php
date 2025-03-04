<?php

class Utils{
  public static function create_json_file($filePath){
    if(!file_exists($filePath)){
      $initialData = ['Tasks' => []];
      file_put_contents($filePath, json_encode($initialData));
    }
  }
}