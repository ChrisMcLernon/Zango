for ((i = 0; i < 4; i++))
do
    nohup locust --config=locust.conf --host="http://app${i}.zelthy.com:8000/" --html "loadtest_results/{$1}/{$2}/loadtest_${i}.html" &
done