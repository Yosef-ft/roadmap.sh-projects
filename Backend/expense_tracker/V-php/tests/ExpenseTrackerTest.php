<?php

namespace App;

use PHPUnit\Framework\TestCase;


class ExpenseTrackerTest extends TestCase
{
    private $tracker;
    private $tempFile;

    protected function setUp(): void
    {
        
        $this->tempFile = tempnam(sys_get_temp_dir(), 'expense_test_');
        file_put_contents($this->tempFile, '{"Expenses": []}');

        $this->tracker = new ExpenseTracker();
        $reflection = new \ReflectionClass($this->tracker);
        $property = $reflection->getProperty('filePath');
        $property->setAccessible(true);
        $property->setValue($this->tracker, $this->tempFile);
    }

    protected function tearDown(): void
    {

        if (file_exists($this->tempFile)) {
            unlink($this->tempFile);
        }
    }

    public function testAddExpense()
    {
        $id = $this->tracker->addExpense("Coffee", 5);
        $this->assertEquals(1, $id);

        $expenses = json_decode(file_get_contents($this->tempFile), true);
        $this->assertCount(1, $expenses['Expenses']);
        $this->assertEquals("Coffee", $expenses['Expenses'][0]['description']);
        $this->assertEquals(5, $expenses['Expenses'][0]['amount']);
        $this->assertEquals(date('Y-m-d'), $expenses['Expenses'][0]['date']);
    }

    public function testUpdateExpense()
    {
        $this->tracker->addExpense("Lunch", 10);
        $this->tracker->updateExpense(1, 15);

        $expenses = json_decode(file_get_contents($this->tempFile), true);
        $this->assertEquals(15, $expenses['Expenses'][0]['amount']);
        $this->assertEquals("Lunch", $expenses['Expenses'][0]['description']);
    }

    public function testDeleteExpense()
    {
        $this->tracker->addExpense("Dinner", 20);
        $this->tracker->addExpense("Movie", 15);
        $this->tracker->deleteExpense(1);

        $expenses = json_decode(file_get_contents($this->tempFile), true);
        $this->assertCount(1, $expenses['Expenses']);
        $this->assertEquals(2, $expenses['Expenses'][0]['id']);
        $this->assertEquals("Movie", $expenses['Expenses'][0]['description']);
    }


    public function testSummaryExpense()
    {
        $this->tracker->addExpense("Gas", 40);
        $this->tracker->addExpense("Food", 20);

        $total = $this->tracker->summaryExpense();
        $this->assertEquals(60, $total);
    }

    public function testMonthlyExpense()
    {
        $this->tracker->addExpense("Rent", 1000);
        $this->tracker->addExpense("Utilities", 200);

        $currentMonth = (new \DateTime())->format('m');
        $monthlyTotal = $this->tracker->monthlyExpense($currentMonth);
        $this->assertEquals(1200, $monthlyTotal);

        $this->assertEquals(0, $this->tracker->monthlyExpense('01'));
    }
}