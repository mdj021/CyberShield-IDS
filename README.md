# CyberShield IDS

Machine Learning Based Intrusion Detection System using Random Forest.

## Features

- Network Intrusion Detection
- Machine Learning Based Detection
- Random Forest Classifier
- Confusion Matrix Generation
- Accuracy, Precision, Recall, F1 Score
- Model Persistence using Joblib

## Technologies

- Python
- Scikit-Learn
- Pandas
- Matplotlib
- Joblib

## Results

Accuracy: 99.86%

## Project Structure

dataset/
models/
screenshots/
src/

## Future Enhancements

- Flask Dashboard
- Real-Time Monitoring
- Wireshark Integration
- Attack Classification
## Network Traffic Features Used

The Intrusion Detection System (IDS) uses 41 network traffic features from the NSL-KDD dataset to classify traffic as either **Normal** or **Attack**.

| No. | Feature Name                |
| --- | --------------------------- |
| 1   | duration                    |
| 2   | protocol_type               |
| 3   | service                     |
| 4   | flag                        |
| 5   | src_bytes                   |
| 6   | dst_bytes                   |
| 7   | land                        |
| 8   | wrong_fragment              |
| 9   | urgent                      |
| 10  | hot                         |
| 11  | num_failed_logins           |
| 12  | logged_in                   |
| 13  | num_compromised             |
| 14  | root_shell                  |
| 15  | su_attempted                |
| 16  | num_root                    |
| 17  | num_file_creations          |
| 18  | num_shells                  |
| 19  | num_access_files            |
| 20  | num_outbound_cmds           |
| 21  | is_host_login               |
| 22  | is_guest_login              |
| 23  | count                       |
| 24  | srv_count                   |
| 25  | serror_rate                 |
| 26  | srv_serror_rate             |
| 27  | rerror_rate                 |
| 28  | srv_rerror_rate             |
| 29  | same_srv_rate               |
| 30  | diff_srv_rate               |
| 31  | srv_diff_host_rate          |
| 32  | dst_host_count              |
| 33  | dst_host_srv_count          |
| 34  | dst_host_same_srv_rate      |
| 35  | dst_host_diff_srv_rate      |
| 36  | dst_host_same_src_port_rate |
| 37  | dst_host_srv_diff_host_rate |
| 38  | dst_host_serror_rate        |
| 39  | dst_host_srv_serror_rate    |
| 40  | dst_host_rerror_rate        |
| 41  | dst_host_srv_rerror_rate    |

These features describe different characteristics of network traffic, such as connection duration, protocol type, bytes transferred, login attempts, error rates, and host-based statistics. The Random Forest classifier uses these features to detect malicious activities and network intrusions.