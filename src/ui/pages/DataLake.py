import streamlit as st
from presentation.controller.azure.DataLakeController import DataLakeController
from presentation.schema.AzureSchema import CreateFileFormObject, UploadFileFormObject


class DataLake:
    
    def __init__(self):
        self.title = 'DataLake'
        self.container = 'io-local'
        self.ctl = DataLakeController()
        

    def view(self):
        st.title(self.title)
        self.container = st.text_input('Container', value=self.container)

        tabs = ['Create File', 'Upload File']
        create_file_tab, upload_file_tab = st.tabs(tabs)
        with create_file_tab:
            self.view_create_file()
        with upload_file_tab:
            self.view_upload_file()
     
    
    
    def view_create_file(self):
        
        form: CreateFileFormObject = CreateFileFormObject(
            file_name='test.json',
            blob={
                'company_id': 'test',
                'type': 'test',
                'data': {
                    'attr': 'test'
                }
            }
        )
        form.file_name = st.text_input('File', value=form.file_name)
        form.blob.company_id = st.text_input('CompanyID', value=form.blob.company_id)
        form.blob.type = st.text_input('Type', value=form.blob.type)
        form.blob.data['attr'] = st.text_input('Attribute', value=form.blob.data['attr'])
        st.json(form.model_dump())
        
        if st.button('Create File'):
            result = self.ctl.create_file(
                container=self.container,
                form=form
            )
            if result:
                st.success('Create File Successfully')
            else:
                st.error('Create File Failed')
        
    def view_upload_file(self): 
        form: UploadFileFormObject = UploadFileFormObject(
            file_name='',
            blob={
                'bytes_data': b''
            }
        )      
        uploaded_file = st.file_uploader(
            label='Upload Json File',
            type=['json'],
            )
        if uploaded_file is not None:
            form.file_name = uploaded_file.name
            form.blob.bytes_data = uploaded_file.read()
            
            if st.button('Upload File'):
                result = self.ctl.upload_file(
                    container=self.container,
                    form=form
                )
                if result:
                    st.success('Upload File Successfully') 
                else:
                    st.error('Upload File Failed')
        