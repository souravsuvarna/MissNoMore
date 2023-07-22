import streamlit as st
import pandas as pd
import preprocess, basic_impute, advance_impute

# st.set_page_config(page_title="The Ramsey Highlights", layout="wide")
css = '''
<style>
    [data-testid="stSidebar"]{
        min-width: 500px;
        max-width: 800px;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

st.markdown("""<h1 style='text-align: center; color: white; font-family:'silver-forte', sans-serif;'>MissNoMore</h1><style>
        h1{
            font-size: 50px;
            vertical-align: super;
            color: rgba(144, 141, 143, 0.9);
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #E9E8E8; font-family:'alata', sans-serif;'>Powerful Missing Value Imputation Tool. No data is sent to a server! All code runs locally in your browser. </p>", unsafe_allow_html=True)
st.title("")

flag = 0
flag_neighbor=0
if uploaded_file is not None:

    # Convert the file-like object to a pandas DataFrame
    try:
        # Data Set Upload and display operation.
        data = preprocess.tocsv(uploaded_file)
        st.subheader('Uploaded DataSet :')
        st.caption(uploaded_file.name)
        st.write(data)
        st.title("")
        uploaded_file.name = uploaded_file.name.replace(".csv", "")
        #Asking Which Operation should be carried out [Basic or Advance]
        operation = st.sidebar.radio(
            "Select Mode of Imputation",
            ('None','Basic', 'Advance'))
        
        #Basic Mode
        if(operation=='Basic'):
            # List of column with NA
            column_with_na = preprocess.null_columns(data)
            selected_column = st.sidebar.selectbox("Select a Column",column_with_na)
            st.sidebar.caption("Note: Columns Names in the selection list are the columns with missing values")
            flag = 1
            # Method of Basic Imputation
            methods_of_basic_imputation = ['Replace With Zero','Mean','Median','Mode','Forward Fill','Backward Fill','Interpolate (Linear)','Interpolate (Quadratic)','Interpolate (Cubic)']
            selected_method = st.sidebar.selectbox("Select a method",methods_of_basic_imputation)
            st.sidebar.caption("Selected method will be applied on the selected column to imputate missing value.")
       
        elif (operation=='Advance'):
            flag = 2
            # Methods for advance imputation
            methods_of_advance_imputation = ['KNN','Iterative','SimpleImputer (Mean)','SimpleImputer (Median)','Random-Forest','Decision Tree','Linear Regression','Random Sampling']
            selected_method = st.sidebar.selectbox("Select a method",methods_of_advance_imputation)
        
        # Validtting neighbors that its >2 & only numeric
        def validate_input(input_str):
            try:
                input_int = int(input_str)
                if input_int >= 2:
                    return True
                else:
                    return False
            except ValueError:
                return False
            
        #Neighbors for KNN
        if(selected_method == "KNN"):
            order = st.sidebar.text_input('Enter the number of neighbors to consider:', '2')
            
            if not validate_input(order):
                flag_neighbor=1
                st.sidebar.warning("Please enter a valid numeric value greater than or equal to 2.")
        
        # Submit Section 
        if st.sidebar.button('Submit'):
            
            if(flag==0):
                st.sidebar.warning("Select a mode")
            
            # Basic Imputation    
            elif (flag==1):
                st.subheader("Imputed DataSet :")
                
                #1. Replace with zero impute
                if(selected_method == 'Replace With Zero'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = basic_impute.replace_with_zero(data,selected_column)
                    st.write(df)
                    
                #2. Mean
                elif (selected_method == 'Mean'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = basic_impute.mean(data,selected_column)
                    st.write(df)
                
                #3. Median
                elif (selected_method == 'Median'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = basic_impute.median(data,selected_column)
                    st.write(df)
                    
                #4. Mode
                elif (selected_method == 'Mode'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = basic_impute.mode(data,selected_column)
                    st.write(df)
                
                #5. Forward Fill
                elif (selected_method == 'Forward Fill'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = basic_impute.forward_fill(data,selected_column)
                    st.write(df)
                
                #6. Backward Fill
                elif (selected_method == 'Backward Fill'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = basic_impute.backward_fill(data,selected_column)
                    st.write(df) 
                
                #7. Interploate (linear)
                elif (selected_method == 'Interpolate (Linear)'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = basic_impute.interpolate_linear(data,selected_column)
                    st.write(df) 
                
                #8. Interpolate (quadratic)
                elif (selected_method == 'Interpolate (Quadratic)'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = basic_impute.interpolate_quadratic(data,selected_column)
                    st.write(df)
                
                #9. Interpolate (cubic)
                elif (selected_method == 'Interpolate (Cubic)'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = basic_impute.interpolate_cubic(data,selected_column)
                    st.write(df)                                                                             
            
            
            #Adavnced Imputation
            elif flag==2:
                st.subheader("Imputed DataSet :")
                
                #1. KNN
                if(selected_method == 'KNN') and flag_neighbor==0:
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = advance_impute.knn(data,int(order))
                    st.write(df)
                
                #2. Iterative
                elif(selected_method == 'Iterative'):
                    st.caption(f"{uploaded_file.name}_{selected_method}.csv")
                    df = advance_impute.iterative(data)
                    st.write(df)
            
                        
            # Download Dataset
            if flag!=0 and flag_neighbor!=1 :        
           
                csv_data = df.to_csv(index=False)
                selected_method = selected_method.replace(" ", "_")
                file_name = f"{uploaded_file.name}_{selected_method}.csv"
                st.download_button(label="Download CSV", data=csv_data, file_name=file_name, mime="text/csv")
        
    except Exception as e:
        st.write("Error loading CSV:", e)
