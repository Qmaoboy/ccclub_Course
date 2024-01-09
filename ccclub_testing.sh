#!/bin/bash

PROGRAM="everybodygaming.py"

rm -f mytest.txt

TEST_CASES_DIR="./手拉手團康遊戲"
for input_file in $TEST_CASES_DIR/*.in; do
    # 產生輸出檔案的名稱，例如，將 ".in" 替換為 ".out"
    output_file="${input_file/.in/.out}"
    echo $output_file
    # 從測試案例中讀取輸入，執行程式，並將輸出保存到 my_output.txt 中
    python $PROGRAM < $input_file > mytest.txt

    # 比較程式輸出與預期輸出
    if diff -q mytest.txt $output_file; then
        echo "Pass: $(basename $input_file)"
    else
        echo "Fail: $(basename $input_file)"
    fi
done

# 清理生成的輸出檔案
rm -f mytest.txt

