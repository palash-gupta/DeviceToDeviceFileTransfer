```
git clone https://github.com/palash-gupta/DeviceToDeviceFileTransfer.git
cd DeviceToDeviceFileTransfer
pip install -r requirements.txt
python app.py --host=0.0.0.0 --port=80
```

- An IP address in the form of 192.168.x.x shows up
- On a different device connected to common network, enter the IP address in a browser.
- Upload all the required files from this device
- In the original device, in the `/uploads` folder in the downloads folder, all the uploaded files are present.
