import streamlit as st
import pandas as pd

def Getdata(substring):
    sheet_id="1NikKhqY7u3AGsm9Fpk9UaqNFyzmyojuz8-iqUGh295g"
    sheet_data="Form Responses 1"

    gsheet_data = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(sheet_id, sheet_data)

    url = gsheet_data.replace(" ","")
    df=pd.read_csv(url, on_bad_lines='skip')
    df=df.iloc[:,:22].fillna('')

    df['Battery In Voltage']=pd.to_numeric(df['Battery In Voltage'])
    df['Battery Out Voltage']=pd.to_numeric(df['Battery Out Voltage'])
    df['Amount ']=pd.to_numeric(df['Amount '])

    data=pd.DataFrame({
                      'Timestamp':df['Timestamp'],'Customer name':df['Customer name'],'Battery_in':df['Battery In'],'Battery_in_volt':df['Battery In Voltage'],'Battery_out':df['Battery Out'],'Battery_Out_volt':df['Battery Out Voltage'],   
                       'Amount':df['Amount '],'Security_amt':df['Security Amount'],'Penalty_amt':df['Penalty Amount '],'Supervisor':df['Shift supervisor'],'Plan':df['Is there any plan?'],
                      'Battery_submit?':df['Is the customer submitting or collecting battery?'],'Center':df['Center']
                       })

    return data

def main():
    st.set_page_config(page_title="Model to filter data", layout="wide")
    data = Getdata("")
    unique_entries = []
    unique_entries.insert(0,"")
    for col in data.select_dtypes(include='object').columns:
        unique_entries += data[col].unique().tolist()
    selected_entry = st.selectbox("Select entry", options=unique_entries)
    filtered_data = data[data.apply(lambda row: any(str(col).lower() == selected_entry.lower() for col in row), axis=1)]

    # substring = st.text_input("Filteration Key")
    # after_filteration = filtered_data[filtered_data.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    st.write(filtered_data)

if __name__ == '__main__':
    main()   
