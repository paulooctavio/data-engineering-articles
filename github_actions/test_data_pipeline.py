from data_pipeline import main


def test_etl_process():
    result = main()
    if result:
        print("Test passed: ETL process completed successfully.")
    else:
        print("Test failed: ETL process did not complete successfully.")
    assert result
