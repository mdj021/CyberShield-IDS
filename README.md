# CyberShield IDS

A Machine Learning and PCAP-Based Intrusion Detection System (IDS) designed to analyze network traffic and detect potential security threats using Random Forest Classification and Packet Analysis.

## Features

* Machine Learning Based Intrusion Detection
* Random Forest Classifier
* NSL-KDD Dataset Support
* Accuracy, Precision, Recall, and F1 Score Evaluation
* Confusion Matrix Generation
* Model Persistence using Joblib
* Flask Web Dashboard
* PCAP File Upload and Analysis
* TCP, UDP, and ICMP Packet Statistics
* Risk Assessment Module
* Cybersecurity Dashboard Interface

## Technologies Used

* Python
* Flask
* Scikit-Learn
* Pandas
* Matplotlib
* Scapy
* Bootstrap 5
* Joblib

## Results

* Model Accuracy: 99.86%
* Confusion Matrix Generated Successfully
* Real-Time PCAP Analysis Support

## Project Structure

```text
CyberShield-IDS
│
├── dataset/
├── models/
├── results/
├── screenshots/
├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   ├── detect.py
│   └── pcap_analyzer.py
│
├── static/
├── templates/
│   ├── index.html
│   └── results.html
│
├── app.py
├── main.py
├── README.md
└── .gitignore
```

## Flask Dashboard Features

* Upload PCAP Files
* Analyze Network Traffic
* Display Packet Statistics
* Generate Risk Assessment
* View Results Through Web Interface

## PCAP Analysis Features

The system analyzes uploaded PCAP files and extracts:

* Total Packets
* TCP Packet Count
* UDP Packet Count
* ICMP Packet Count
* Risk Level Assessment

### Risk Levels

* HIGH → Possible UDP Flood Attack
* MEDIUM → Heavy TCP Traffic Detected
* LOW → Traffic Appears Normal

## Network Traffic Features Used

The machine learning model uses 41 network traffic features from the NSL-KDD dataset to classify traffic as Normal or Attack.

Examples include:

* duration
* protocol_type
* service
* flag
* src_bytes
* dst_bytes
* logged_in
* count
* srv_count
* dst_host_count
* dst_host_srv_count
* dst_host_rerror_rate

(Complete list available in project documentation.)

## How to Run

### Train Model

```bash
python src/train_model.py
```

### Launch Dashboard

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

### Upload PCAP File

1. Open the dashboard.
2. Upload a `.pcap` file captured using Wireshark.
3. View packet statistics and risk assessment.

## Future Enhancements

* Real-Time Packet Monitoring
* Machine Learning-Based PCAP Classification
* Live Attack Alerts
* Network Visualization Dashboard
* Attack Type Classification
* Downloadable Security Reports
* Email Alert System
