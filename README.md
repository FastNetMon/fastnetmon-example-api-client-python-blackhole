# FastNetMon Advanced example API client which blocks and unblocks IP

This example script can create blackhole announce, list blocked hosts and remove it using UUID lookup.

To use this example, please enable API using this [guide](https://fastnetmon.com/advanced-api/) and install dependencies for it:
```
sudo apt-get install -y python3-requests
```

And download fastnetmon_api_client.py from GitHub:
```
wget https://raw.githubusercontent.com/FastNetMon/fastnetmon-example-api-client-python-blackhole/main/fastnetmon_api_client.py
```

Enable execution flag:
```
chmod +x fastnetmon_api_client.py
```

And run it this way:
```
./fastnetmon_api_client.py
```

Valid output looks like:
```Blackhole IP: 127.0.0.197
Correctly blackholed IP
Wait 5 second to propagate changes
Correctly found UUID for this IP 2518758c-a751-4984-9aeb-c5a935422e91
Correctly removed blackhole announce
```
