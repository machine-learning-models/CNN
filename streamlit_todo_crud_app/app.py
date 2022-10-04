import streamlit as st

import pandas as pd

import plotly.express as px

from db_fxns import (create_table, add_data, view_all_data, get_task,
                    view_unique_tasks, edit_task_data, delete_data)

def main():
    st.title('ToDo App with Streamlit')
    
    menu = ['Create', 'Read', 'Update', 'Delete', 'About']
    choice = st.sidebar.selectbox('Menu', menu)
    #selection = ['Create', 'Read', 'Update', 'Delete']

    create_table()
    
    if choice == 'Create':
        st.subheader('Add Item')

        col1, col2 = st.columns(2)

        with col1:
            task = st.text_area('Task To Do')

        with col2:
            task_status = st.selectbox('Status', ['ToDo', 'Doing', 'Done'])
            task_due_date = st.date_input('Due Date')

        if st.button('Add Task'):
            add_data(task, task_status, task_due_date)
            st.success('Successfully Added Data: {}'.format(task))
            
            #st.input('Please Enter Your Task')
            #if selection == 'Create'
        
    elif choice == 'Read':
        st.subheader('View Items')
        result = view_all_data()
        st.write(result)
        df = pd.DataFrame(result, columns = ['Task', 'Status', 'Due Date'])
        with st.expander('View All Data'):
            st.dataframe(df)

        with st.expander('Task Status'):
            task_df = df['Status'].value_counts().to_frame()
            #st.dataframe(task_df)
            task_df = task_df.reset_index() 
            st.dataframe(task_df)

            # Distribution of Values => Pie Chart
            p1 = px.pie(task_df, names = 'index', values = 'Status')
            st.plotly_chart(p1)
        

    elif choice == 'Update':
        st.subheader('Edit/Update Items')
        
        # First View Your Data
        result = view_all_data()
        df = pd.DataFrame(result, columns = ['Task', 'Status', 'Due Date'])
        with st.expander('Current Data'):
            st.dataframe(df)

        # Edit Data
        #st.write(view_unique_tasks())
        # Just the List Element 0, Not List in List
        list_of_task = [i[0] for i in view_unique_tasks()]
        #st.write(list_of_task)

        selected_task = st.selectbox('Task To Edit', list_of_task)

        selected_result = get_task(selected_task)
        st.write(selected_result)
        if selected_result:

            task = selected_result[0][0]
            task_status = selected_result[0][1]
            task_due_date = selected_result[0][2]

            #st.write(task, task_status, task_due_date)

            col1, col2 = st.columns(2)

            with col1:
                new_task = st.text_area('Task To Do', task)

            with col2:
                new_task_status = st.selectbox(task_status, ['ToDo', 'Doing', 'Done'])
                new_task_due_date = st.date_input(task_due_date)

            if st.button('Update Task'):
                edit_task_data( new_task, new_task_status, new_task_due_date, task, task_status, task_due_date)
                
                st.success('Successfully Updated:: {} To ::{}'.format(task, new_task))

        result2 = view_all_data()
        df2 = pd.DataFrame(result2, columns = ['Task', 'Status', 'Due Date'])
        with st.expander('Updated Data'):
            st.dataframe(df2)             
        
    elif choice == 'Delete':
        st.subheader('Delete Item')
        result = view_all_data()
        df = pd.DataFrame(result, columns = ['Task', 'Status', 'Due Date'])
        with st.expander('Current Data'):
            st.dataframe(df)

        list_of_task = [i[0] for i in view_unique_tasks()]
        selected_task = st.selectbox('Task To Delete', list_of_task)
        st.warning('Do You want to Delete {}'.format(selected_task))
        if st.button('Delete Task') :
            delete_data(selected_task)
            st.success('Task has been Successfully Deleted')

        new_result = view_all_data()
        df2 = pd.DataFrame(new_result, columns = ['Task', 'Status', 'Due Date'])
        with st.expander('Updated Data'):
            st.dataframe(df2)
        
    else:
        st.subheader('About')
        st.info('Built with Streamlit')
        st.info('by SH')
        st.text('Stephan')

if __name__ == '__main__':
    main()
