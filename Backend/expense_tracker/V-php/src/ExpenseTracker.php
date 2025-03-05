<?php

namespace App;

class ExpenseTracker{
    private $filePath;

    function __construct(){
      
      $dirName = dirname(__DIR__) . '/data';
      $this->filePath = $dirName . '/expenses.json';

      if(!file_exists($dirName)){
        mkdir($dirName, 0777, true);
      }
      
      Utils::create_json_file($this->filePath); 
    }  


    function addExpense(string $description, float $amount){
      $expenses = json_decode(file_get_contents($this->filePath), true);

      if ($expenses['Expenses']== null){
        $expenses = ['Expenses' => []];
      }

      $id_len = count($expenses['Expenses'] ?? []);

      $newExpense = [
        "id" => $id_len + 1, 
        "date" => date('Y-m-d'),
        "description" => $description,
        "amount" => $amount
      ];

      $expenses['Expenses'][] = $newExpense;
      
      file_put_contents($this->filePath, json_encode($expenses, JSON_PRETTY_PRINT));
      
      return $newExpense['id'];
    }

    function updateExpense(int $id, float $amount){
      $expenses = json_decode(file_get_contents($this->filePath), true);

      foreach($expenses['Expenses'] as &$expense){
        if($expense['id'] == $id){
          $expense['amount'] = $amount;
          break;
        }
      }
      file_put_contents($this->filePath,json_encode($expenses, JSON_PRETTY_PRINT));
    }

    function deleteExpense(int $id){
      $expenses = json_decode(file_get_contents($this->filePath), true);

      foreach($expenses['Expenses'] as $key => $expense){
        if($expense['id'] == $id){
          unset($expenses['Expenses'][$key]);
          $expenses['Expenses'] = array_values($expenses['Expenses']);
          break;
        }
      }

      file_put_contents($this->filePath, json_encode($expenses, JSON_PRETTY_PRINT));
    }


    function listExpenses(){
      $expenses = json_decode(file_get_contents($this->filePath), true);

      echo PHP_EOL;

      echo 'ID  |  DATE  |  Description  |  Amount' . PHP_EOL;
      echo '---------------------------------------------' . PHP_EOL;
      
      foreach ($expenses['Expenses'] as $expense) {
          echo $expense['id'] . '  |  ' . $expense['date'] . ' |  ' . $expense['description'] . ' |  ' . $expense['amount'] . PHP_EOL;
      }
    }


    function summaryExpense(){
      $expenses = json_decode(file_get_contents($this->filePath), true);

      $totalExpense = 0;

      foreach($expenses['Expenses'] as $expense){
        $totalExpense += $expense['amount'];
      }

      return $totalExpense;
    }


    function monthlyExpense($summaryMonth){
      $expenses = json_decode(file_get_contents($this->filePath), true);

      $expenseSummary = 0;

      foreach ($expenses['Expenses'] as $expense) {
          $date = new \DateTime($expense['date']);
          $month = $date->format('m');
          if ($summaryMonth == $month) {
              $expenseSummary += $expense['amount'];
          }
      }

      return $expenseSummary;
    }
 
}
