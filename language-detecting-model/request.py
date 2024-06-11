import requests

# An example to test that the server works correctly.
# It takes one sample for each Iris type, requests prediction and compares it with the right target
if __name__ == '__main__':
    y = 'C++'
    features = {
        "text": '#include <iostream>\nint main(){\nstd::cout<<"Hello, world";\nreturn 0;\n}'
    }
    resp = requests.post(
        "http://127.0.0.1:80/predict",
        json=features
    )
    file = open("resp.txt", "w")
    file.write(str(resp.json()))
    print(f"Input features: {features}")
    print(f"Predicted: {resp.json()}")
    print(f"Expected: {y}")
    print("----")
