<?php

namespace App;

class Utils{
  public static function create_json_file($fileName){
    if(!file_exists($fileName)){
      $initialData = ['Expenses'=> []];
      file_put_contents($fileName, json_encode($initialData, JSON_PRETTY_PRINT));
    }
  }
}