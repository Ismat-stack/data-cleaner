# 🧹 Data Cleaner / Preprocessor (Streamlit App)

A simple and interactive **Streamlit web app** that helps you **clean, preprocess, and normalize datasets** without writing a single line of code.
You can upload your CSV or Excel file, handle missing values, remove duplicates, normalize data, and then **download the cleaned version** instantly.


## 🚀 Features

✅ Upload **CSV** or **Excel** files

✅ Handle **missing values**

✅ Remove **duplicate rows**

✅ Apply **Min–Max normalization** to numeric columns

✅ Preview both **original and cleaned data**

✅ Download cleaned data as a **CSV file**


## 🧰 Technologies Used

* [Streamlit](https://streamlit.io/) – interactive web interface
* [Pandas](https://pandas.pydata.org/) – data manipulation and preprocessing


## 📦 Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/ismat-data/data-cleaner.git
   cd data-cleaner
   ```

2. **(Optional) Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Mac/Linux
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## 📋 Requirements File (`requirements.txt`)

If you don’t have one yet, create a file named `requirements.txt` containing:

```
streamlit
pandas
openpyxl
```


## ▶️ Run the App

To start the Streamlit app, run:

```bash
streamlit run data_cleaner.py
```

Then open your browser and go to:
👉 **[http://localhost:8501](http://localhost:8501)**


## ⚙️ How to Use

1. **Upload your data file** (`.csv` or `.xlsx`)
2. **View original data** (first few rows shown)
3. **Handle missing values:**

   * Drop rows with missing data
   * Fill with mean or median (for numeric columns)
   * Fill with a custom value
4. **Remove duplicates** (optional)
5. **Normalize numeric columns** using Min–Max scaling (optional)
6. **Preview cleaned data**
7. **Download the cleaned dataset** as a CSV file


## 🧮 Example Workflow

1. Upload a file like `sales_data.csv`
2. Drop rows with missing values
3. Remove duplicates
4. Apply Min–Max scaling
5. Download the cleaned dataset as `cleaned_data.csv`


## 🧩 Customization

You can extend this app easily:

* Add **standardization (z-score scaling)**
* Add **column type conversions**
* Add **outlier detection/removal**
* Integrate with a **database** or **data visualization dashboard**


## 🐞 Troubleshooting

| Problem            | Possible Cause             | Solution                              |
| ------------------ | -------------------------- | ------------------------------------- |
| File not uploading | Wrong file type            | Ensure file is `.csv` or `.xlsx`      |
| Encoding error     | Special characters in data | Use UTF-8 encoding                    |
| App not launching  | Missing dependencies       | Run `pip install -r requirements.txt` |


## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.


## 💡 Author

**Khan Ismat**

🔗 [ismat-data](https://github.com/ismat-data)
