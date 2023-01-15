import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()



st.title("SitaADS flow :")
st.write("Please upload your csv file to view the whole flow and dashboard")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    TextFileReader = pd.read_csv(uploaded_file, chunksize=1000)
    dfList = []
    for df in TextFileReader:
        dfList.append(df)

    df = pd.concat(dfList,sort=False)

    st.session_state["df"] = df

    st.write(df)
    df['datetime'] = pd.to_datetime(df.Date.astype(str)+' '+df.Time.astype(str))
    df["Label"] = df["Level"].apply(lambda x: int(x != "INFO"))
    df['timestamp'] = df["datetime"].values.astype(np.int64) // 10 ** 9

    ax = sns.countplot(x ='Level', data = df)
    ax.set(title='Number of Normal (0) and Abnormal Sequences (1) ')
    for p in ax.patches:
        height = p.get_height()
        ax.text(x = p.get_x()+(p.get_width()/2), 
        y = height+10,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
    plt.show()
    plt.savefig('count_plot')
    st.write("Level towards Count plot")
    st.image("count_plot.png")
    plt.figure()

    df_normal = df[df["Label"] == 0]
    df_abnormal = df[df["Label"] == 1]

    st.session_state["df_abnormal"] = df_abnormal

    
    bx = sns.countplot(x ='Port Number', data = df_abnormal, order=df_abnormal.value_counts(df_abnormal['Port Number']).iloc[:3].index)
    bx.set(title='Top 3 port number that contains anomaly')
    for p in bx.patches:
        height = p.get_height()
        bx.text(x = p.get_x()+(p.get_width()/2), 
        y = height+2,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
        plt.savefig('count_plot_port')
    st.write("Plot Based Port Number")
    st.image("count_plot_port.png")
    plt.figure()

        
    cx = sns.countplot(x ='Module Name', data = df_abnormal, order=df_abnormal.value_counts(df_abnormal['Module Name']).iloc[:3].index)
    cx.set(title='Top 3 Module Name that contains anomaly')
    for p in cx.patches:
        height = p.get_height()
        cx.text(x = p.get_x()+(p.get_width()/2), 
        y = height+2,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
        plt.savefig('count_plot_modulename')
    st.write("Plot Based Module Name")
    st.image("count_plot_modulename.png")
    plt.figure()

    dx = sns.countplot(x ='Time', data = df_abnormal, order=df_abnormal.value_counts(df_abnormal['Time']).iloc[:3].index)
    dx.set(title='Top 3 Time that contains anomaly')
    for p in dx.patches:
        height = p.get_height()
        dx.text(x = p.get_x()+(p.get_width()/2), 
        y = height,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
        plt.savefig('count_plot_time')
    st.write("Plot Based Time")
    st.image("count_plot_time.png")
    plt.figure()

    ex = sns.countplot(x ='Database', data = df_abnormal, order=df_abnormal.value_counts(df_abnormal['Database']).iloc[:3].index)
    ex.set(title='Top 3 Database that contains anomaly')
    for p in ex.patches:
        height = p.get_height()
        ex.text(x = p.get_x()+(p.get_width()/2), 
        y = height,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
        plt.savefig('count_plot_database')
    st.write("Plot Based Database")
    st.image("count_plot_database.png")
    plt.figure()

    df.loc[(df['Port Number'] != 1363) & (df['Port Number'] != 1376) & (df['Port Number'] != 1364), 'CatPortNumber'] = 4
    df.loc[df['Port Number'] == 1363, 'CatPortNumber'] = 1
    df.loc[df['Port Number'] == 1376, 'CatPortNumber'] = 2
    df.loc[df['Port Number'] == 1364, 'CatPortNumber'] = 3
    df.loc[(df['Module Name'] == 'openerp.modules.graph:'), 'CatModuleName'] = 1
    df.loc[(df['Module Name'] == 'openerp.sql_db:'), 'CatModuleName'] = 2
    df.loc[(df['Module Name'] == 'openerp.http:'), 'CatModuleName'] = 3
    df.loc[(df['Module Name'] == 'openerp.addons.base.ir.ir_ui_view:'), 'CatModuleName'] = 4
    df.loc[(df['Module Name'] == 'openerp.models:'), 'CatModuleName'] = 5
    df.loc[(df['Module Name'] == 'openerp.addons.email_template.email_template:'), 'CatModuleName'] = 6
    df.loc[(df['Module Name'] == 'openerp.addons.base.ir.ir_ui_model:'), 'CatModuleName'] = 7
    df.loc[(df['Module Name'] == 'openerp.addons.base.ir.ir_mail_server:'), 'CatModuleName'] = 8
    df.loc[(df['Module Name'] == 'openerp.addons.mail.mail_mail:'), 'CatModuleName'] = 9
    df.loc[(df['Module Name'] == 'openerp.addons.website.model.ir_http:'), 'CatModuleName'] = 10
    df.loc[(df['Module Name'] == 'werkzeug:'), 'CatModuleName'] = 11
    df.loc[(df['Module Name'] == 'openerp.addons.document.std_index:'), 'CatModuleName'] = 12
    df.loc[(df['Module Name'] != 'openerp.modules.graph:') & (df['Module Name'] != 'openerp.sql_db:') & (df['Module Name'] != 'openerp.http:')& (df['Module Name'] != 'openerp.addons.base.ir.ir_ui_view:')& (df['Module Name'] != 'openerp.models:')& (df['Module Name'] != 'openerp.addons.email_template.email_template:')& (df['Module Name'] != 'openerp.addons.base.ir.ir_ui_model:')& (df['Module Name'] != 'openerp.addons.base.ir.ir_mail_server:')& (df['Module Name'] != 'openerp.addons.mail.mail_mail:')& (df['Module Name'] != 'openerp.addons.website.model.ir_http:')& (df['Module Name'] != 'werkzeug:')& (df['Module Name'] != 'openerp.addons.document.std_index:'), 'CatModuleName'] = 13
    df.loc[(df['Time'] == '06:44:20,782'), 'CatTime'] = 1
    df.loc[(df['Time'] == '06:44:12,466'), 'CatTime'] = 2
    df.loc[(df['Time'] == '02:22:35,163'), 'CatTime'] = 3
    df.loc[(df['Time'] == '08:15:58,341'), 'CatTime'] = 4
    df.loc[(df['Time'] == '03:59:30,893'), 'CatTime'] = 5
    df.loc[(df['Time'] == '08:15:58,340'), 'CatTime'] = 6
    df.loc[(df['Time'] == '06:44:12,465'), 'CatTime'] = 7
    df.loc[(df['Time'] == '06:29:38,212'), 'CatTime'] = 8
    df.loc[(df['Time'] == '03:59:30,892'), 'CatTime'] = 9
    df.loc[(df['Time'] == '06:44:20,781'), 'CatTime'] = 10
    df.loc[(df['Time'] == '06:29:38,213'), 'CatTime'] = 11
    df.loc[(df['Time'] == '02:22:35,164'), 'CatTime'] = 12
    df.loc[(df['Time'] == '08:20:13,089'), 'CatTime'] = 13
    df.loc[(df['Time'] == '04:37:26,273'), 'CatTime'] = 14
    df.loc[(df['Time'] == '02:22:35,162'), 'CatTime'] = 15
    df.loc[(df['Time'] != '06:44:20,782') & (df['Time'] != '06:44:12,466') & (df['Time'] != '02:22:35,163')& (df['Time'] != '08:15:58,341')& (df['Time'] != '03:59:30,893')& (df['Time'] != '08:15:58,340')& (df['Time'] != '06:44:12,465')& (df['Time'] != '06:29:38,212')& (df['Time'] != '03:59:30,892')& (df['Time'] != '06:44:20,781')& (df['Time'] != '06:29:38,213')& (df['Time'] != '02:22:35,164')& (df['Time'] != '08:20:13,089')&(df['Time'] != '04:37:26,273')&(df['Time'] != '02:22:35,162'), 'CatTime'] = 16
    df.loc[(df['Database'] == 'SNM_After_June_2018'), 'CatDatabase'] = 1
    df.loc[(df['Database'] == 'SO_ELK'), 'CatDatabase'] = 2
    df.loc[(df['Database'] == 'smoffice_hotel'), 'CatDatabase'] = 3
    df.loc[(df['Database'] == '?'), 'CatDatabase'] = 4
    df.loc[(df['Database'] != 'SNM_After_June_2018') & (df['Database'] != 'SO_ELK') & (df['Database'] != 'smoffice_hotel')& (df['Database'] != '?')] = 5
    df.loc[(df['Date'] == '3/02/2022'), 'CatDate'] = 1
    df.loc[(df['Date'] == '7/02/2022'), 'CatDate'] = 2
    df.loc[(df['Date'] == '10/02/2022'), 'CatDate'] = 3
    df.loc[(df['Date'] == '14/02/2022'), 'CatDate'] = 4
    df.loc[(df['Date'] == '15/02/2022'), 'CatDate'] = 5
    df.loc[(df['Date'] == '17/02/2022'), 'CatDate'] = 6
    df.loc[(df['Date'] == '18/02/2022'), 'CatDate'] = 7
    df.loc[(df['Date'] == '21/02/2022'), 'CatDate'] = 8
    df.loc[(df['Date'] == '22/02/2022'), 'CatDate'] = 9
    df.loc[(df['Date'] == '23/02/2022'), 'CatDate'] = 10
    df.loc[(df['Date'] == '24/02/2022'), 'CatDate'] = 11
    df.loc[(df['Date'] == '28/02/2022'), 'CatDate'] = 12
    df.loc[(df['Date'] != '3/02/2022') & (df['Date'] != '7/02/2022') & (df['Date'] != '10/02/2022')& (df['Date'] != '14/02/2022')& (df['Date'] != '15/02/2022')& (df['Date'] != '17/02/2022')& (df['Date'] != '18/02/2022')& (df['Date'] != '21/02/2022')& (df['Date'] != '22/02/2022')& (df['Date'] != '23/02/2022')& (df['Date'] != '24/02/2022')& (df['Date'] != '28/02/2022'), 'CatDate'] = 13

    df_prediction = df[["CatPortNumber",'CatModuleName',"CatTime","CatDatabase","CatDate","Label"]]
    st.write(df_prediction)
    fig, ax = plt.subplots(figsize=(10,10))
    sns.heatmap(df_prediction.corr(),square = True,ax=ax)
    plt.savefig('heatmap')
    st.write("Variable Correlation Heatmap")

    st.image("heatmap.png")
    plt.figure()

    df_prediction_normal = df_prediction[df_prediction["Label"] == 0]
    df_prediction_abnormal = df_prediction[df_prediction["Label"] == 1]
    st.session_state["df_prediction_abnormal"] = df_prediction_abnormal

    df_sample_prediction_normal = df_prediction_normal.sample(n=153)

    df_prediction_sample = pd.concat([df_sample_prediction_normal , df_prediction_abnormal])

    #decision tree
    from sklearn.model_selection import train_test_split
    X_tree = df_prediction_sample.drop(['Label'], axis=1)

    y_tree = df_prediction_sample['Label']

    X_train_tree, X_test_tree, y_train_tree, y_test_tree = train_test_split(X_tree, y_tree, test_size = 0.2, random_state = 42)

    # instantiate the DecisionTreeClassifier model with criterion gini index
    from sklearn.tree import DecisionTreeClassifier
    clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)


    # fit the model
    clf_gini.fit(X_train_tree, y_train_tree)

    y_pred_gini_tree = clf_gini.predict(X_test_tree)

    from sklearn.metrics import accuracy_score

    st.write('============================================================================')

    st.write("Model 1 Result : Decision Tree")

    st.write('Model accuracy score : {0:0.4f}'. format(accuracy_score(y_test_tree, y_pred_gini_tree)))

    y_pred_train_gini_tree = clf_gini.predict(X_train_tree)

    st.write('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train_tree, y_pred_train_gini_tree)))

    st.write('Training set score: {:.4f}'.format(clf_gini.score(X_train_tree, y_train_tree)))

    st.write('Test set score: {:.4f}'.format(clf_gini.score(X_test_tree, y_test_tree)))


    from sklearn.metrics import confusion_matrix,precision_score, recall_score, f1_score


    cm_tree = confusion_matrix(y_test_tree,y_pred_gini_tree)

    st.write('Confusion matrix for Decision Tree n\n', cm_tree)

    st.write('\nTrue Positives(TP) = ', cm_tree[0,0])

    st.write('\nTrue Negatives(TN) = ', cm_tree[1,1])

    st.write('\nFalse Positives(FP) = ', cm_tree[0,1])

    st.write('\nFalse Negatives(FN) = ', cm_tree[1,0])

    cm_matrix_tree = pd.DataFrame(data=cm_tree, columns=['Actual Positive:1', 'Actual Negative:0'], 
                                 index=['Predict Positive:1', 'Predict Negative:0'])

    sns.heatmap(cm_matrix_tree, annot=True, fmt='d', cmap='YlGnBu')
    plt.savefig('cmtreemap')
    st.write("Confusion Matrix for Decision Tree (Diagram Form)")
    st.image("cmtreemap.png")
    plt.figure()

    st.write("Decision Tree score : ")
    st.write("Precision Score = ", precision_score(y_test_tree, y_pred_gini_tree))
    st.write("Recall Score = ", recall_score(y_test_tree, y_pred_gini_tree))
    st.write("F1 Score = ", f1_score(y_test_tree, y_pred_gini_tree))

    DTPrecisionScore = precision_score(y_test_tree, y_pred_gini_tree)
    DTRecallScore = recall_score(y_test_tree, y_pred_gini_tree)
    DTF1Score = f1_score(y_test_tree, y_pred_gini_tree)
    
#later need to add graph here

    from sklearn import tree

    tree.plot_tree(clf_gini.fit(X_train_tree, y_train_tree)) 
    plt.savefig('plot_tree')
    st.write("Decision Tree map")

    st.image("plot_tree.png")
    plt.figure()

    st.write('============================================================================')
    st.write("Model 2 Result : Logistic Regression")
    from sklearn.model_selection import train_test_split
    X_logreg = df_prediction_sample.drop(['Label'], axis=1)

    y_logreg = df_prediction_sample['Label']

    X_train_logreg, X_test_logreg, y_train_logreg, y_test_logreg = train_test_split(X_logreg, y_logreg, test_size = 0.2, random_state = 42)
    from sklearn.linear_model import LogisticRegression


    # instantiate the model
    logreg = LogisticRegression(solver='liblinear', random_state=0)


    # fit the model
    logreg.fit(X_train_logreg, y_train_logreg)

    y_pred_test_logreg = logreg.predict(X_test_logreg)
    proba1 = logreg.predict_proba(X_test_logreg)[:,0]
    proba2 = logreg.predict_proba(X_test_logreg)[:,1]
    from sklearn.metrics import accuracy_score

    st.write('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test_logreg, y_pred_test_logreg)))
    y_pred_train_logreg = logreg.predict(X_train_logreg)
    st.write('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train_logreg, y_pred_train_logreg)))
    st.write('Training set score: {:.4f}'.format(logreg.score(X_train_logreg, y_train_logreg)))

    st.write('Test set score: {:.4f}'.format(logreg.score(X_test_logreg, y_test_logreg)))
    from sklearn.metrics import confusion_matrix
    cm_logreg = confusion_matrix(y_test_logreg, y_pred_test_logreg)

    st.write('Confusion matrix for Logistic Regression n\n', cm_logreg)

    st.write('\nTrue Positives(TP) = ', cm_logreg[0,0])

    st.write('\nTrue Negatives(TN) = ', cm_logreg[1,1])

    st.write('\nFalse Positives(FP) = ', cm_logreg[0,1])

    st.write('\nFalse Negatives(FN) = ', cm_logreg[1,0])

    cm_matrix_logreg = pd.DataFrame(data=cm_logreg, columns=['Actual Positive:1', 'Actual Negative:0'], 
                                 index=['Predict Positive:1', 'Predict Negative:0'])

    sns.heatmap(cm_matrix_logreg, annot=True, fmt='d', cmap='YlGnBu')
    plt.savefig('lrtreemap')
    st.write("Confusion Matrix for Logistic Regression (Diagram Form)")
    st.image("lrtreemap.png")
    plt.figure()

    st.write("Logistic Regression score : ")
    st.write("Precision Score = ", precision_score(y_test_logreg, y_pred_test_logreg))
    st.write("Recall Score = ", recall_score(y_test_logreg, y_pred_test_logreg))
    st.write("F1 Score = ", f1_score(y_test_logreg, y_pred_test_logreg))

    LRPrecisionScore = precision_score(y_test_logreg, y_pred_test_logreg)
    LRRecallScore = recall_score(y_test_logreg, y_pred_test_logreg)
    LRF1Score = f1_score(y_test_logreg, y_pred_test_logreg)

    st.write('============================================================================')
    st.write("Model 3 Result : Support Vector Machine")

    from sklearn.model_selection import train_test_split
    X_svm = df_prediction_sample.drop(['Label'], axis=1)

    y_svm = df_prediction_sample['Label']

    X_train_svm, X_test_svm, y_train_svm, y_test_svm = train_test_split(X_svm, y_svm, test_size = 0.2, random_state = 42)

        # import SVC classifier
    from sklearn.svm import SVC


    # import metrics to compute accuracy
    from sklearn.metrics import accuracy_score


    # instantiate classifier with default hyperparameters
    svc=SVC() 


    # fit classifier to training set
    svc.fit(X_train_svm,y_train_svm)


    # make predictions on test set
    y_pred_test_svm =svc.predict(X_test_svm)


    # compute and print accuracy score
    st.write('Model accuracy score with default hyperparameters: {0:0.4f}'. format(accuracy_score(y_test_svm, y_pred_test_svm)))

    from sklearn.metrics import confusion_matrix

    cm_svm = confusion_matrix(y_test_svm, y_pred_test_svm)

    

    st.write('Confusion matrix for SVM n\n', cm_svm)

    st.write('\nTrue Positives(TP) = ', cm_svm[0,0])

    st.write('\nTrue Negatives(TN) = ', cm_svm[1,1])

    st.write('\nFalse Positives(FP) = ', cm_svm[0,1])

    st.write('\nFalse Negatives(FN) = ', cm_svm[1,0])

    cm_matrix_svm = pd.DataFrame(data=cm_svm, columns=['Actual Positive:1', 'Actual Negative:0'], 
                                 index=['Predict Positive:1', 'Predict Negative:0'])

    sns.heatmap(cm_matrix_svm, annot=True, fmt='d', cmap='YlGnBu')
    plt.savefig('svmmap')
    st.write("Confusion Matrix for Support Vector Machine (Diagram Form)")
    st.image("svmmap.png")
    plt.figure()

    st.write("Support Vector Machine score : ")
    st.write("Precision Score = ", precision_score(y_test_svm, y_pred_test_svm))
    st.write("Recall Score = ", recall_score(y_test_svm, y_pred_test_svm))
    st.write("F1 Score = ", f1_score(y_test_svm, y_pred_test_svm))

    SVMPrecisionScore = precision_score(y_test_svm, y_pred_test_svm)
    SVMRecallScore = recall_score(y_test_svm, y_pred_test_svm)
    SVMF1Score = f1_score(y_test_svm, y_pred_test_svm)

    st.write('============================================================================')

    st.write("Model Evaluation")

#####################
    # creating the dataset
    data = {'Precision':DTPrecisionScore , 'Recall':DTRecallScore , 'F1':DTF1Score}
    score = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))

    
    # creating the bar plot
    plots = plt.bar(score, values, color ='red',
            width = 0.4)
    for bar in plots.patches:
        plt.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 8),
                   textcoords='offset points')
    plt.title("Decision Tree")
    plt.show()
    plt.savefig('DTresult.png')
    st.write("Results for Decision Tree with Dataset")
    st.image("DTresult.png")
    plt.figure()
#####################
    # creating the dataset
    data1 = {'Precision':LRPrecisionScore , 'Recall':LRRecallScore , 'F1':LRF1Score}
    score1 = list(data1.keys())
    values1 = list(data1.values())
    
    fig = plt.figure(figsize = (10, 5))

    
    # creating the bar plot
    plots = plt.bar(score1, values1, color ='blue',
            width = 0.4)
    for bar in plots.patches:
        plt.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 8),
                   textcoords='offset points')
    plt.title("Logistic Regression")
    plt.show()
    plt.savefig('LRresult.png')
    st.write("Results for Logistic Regression with Dataset")
    st.image("LRresult.png")
    plt.figure()

#####################
    # creating the dataset
    data2 = {'Precision':SVMPrecisionScore , 'Recall':SVMRecallScore , 'F1':SVMF1Score}
    score2 = list(data2.keys())
    values2 = list(data2.values())
    
    fig = plt.figure(figsize = (10, 5))

    
    # creating the bar plot
    plots = plt.bar(score2, values2, color ='orange',
            width = 0.4)
    for bar in plots.patches:
        plt.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 8),
                   textcoords='offset points')
    plt.title("Support Vector Machine(SVM)")
    plt.show()
    plt.savefig('SVMresult.png')
    st.write("Results for Support Vector Machine(SVM) with Dataset")
    st.image("SVMresult.png")
    plt.figure()
    

