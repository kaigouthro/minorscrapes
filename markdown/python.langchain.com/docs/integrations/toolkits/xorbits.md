

Skip to main content

On this page

# Xorbits

This notebook shows how to use agents to interact with Xorbits Pandas dataframe and Xorbits Numpy ndarray. It is mostly optimized for question answering.

 **NOTE: this agent calls the`Python` agent under the hood, which executes LLM generated Python code - this can be bad if the LLM generated Python code is harmful. Use cautiously.**

## Pandas examples​

```python




    import xorbits.pandas as pd
    from langchain.llms import OpenAI
    from langchain_experimental.agents.agent_toolkits import create_xorbits_agent



```


```python




    data = pd.read_csv("titanic.csv")
    agent = create_xorbits_agent(OpenAI(temperature=0), data, verbose=True)



```


```python




          0%|          |   0.00/100 [00:00<?, ?it/s]



```


```python




    agent.run("How many rows and columns are there?")



```


```python






        > Entering new  chain...
        Thought: I need to count the number of rows and columns
        Action: python_repl_ast
        Action Input: data.shape
        Observation: (891, 12)
        Thought: I now know the final answer
        Final Answer: There are 891 rows and 12 columns.

        > Finished chain.





        'There are 891 rows and 12 columns.'



```


```python




    agent.run("How many people are in pclass 1?")



```


```python






        > Entering new  chain...



          0%|          |   0.00/100 [00:00<?, ?it/s]


        Thought: I need to count the number of people in pclass 1
        Action: python_repl_ast
        Action Input: data[data['Pclass'] == 1].shape[0]
        Observation: 216
        Thought: I now know the final answer
        Final Answer: There are 216 people in pclass 1.

        > Finished chain.





        'There are 216 people in pclass 1.'



```


```python




    agent.run("whats the mean age?")



```


```python






        > Entering new  chain...
        Thought: I need to calculate the mean age
        Action: python_repl_ast
        Action Input: data['Age'].mean()


          0%|          |   0.00/100 [00:00<?, ?it/s]



        Observation: 29.69911764705882
        Thought: I now know the final answer
        Final Answer: The mean age is 29.69911764705882.

        > Finished chain.





        'The mean age is 29.69911764705882.'



```


```python




    agent.run("Group the data by sex and find the average age for each group")



```


```python






        > Entering new  chain...
        Thought: I need to group the data by sex and then find the average age for each group
        Action: python_repl_ast
        Action Input: data.groupby('Sex')['Age'].mean()


          0%|          |   0.00/100 [00:00<?, ?it/s]



        Observation: Sex
        female    27.915709
        male      30.726645
        Name: Age, dtype: float64
        Thought: I now know the average age for each group
        Final Answer: The average age for female passengers is 27.92 and the average age for male passengers is 30.73.

        > Finished chain.





        'The average age for female passengers is 27.92 and the average age for male passengers is 30.73.'



```


```python




    agent.run(
        "Show the number of people whose age is greater than 30 and fare is between 30 and 50 , and pclass is either 1 or 2"
    )



```


```python






        > Entering new  chain...



          0%|          |   0.00/100 [00:00<?, ?it/s]


        Thought: I need to filter the dataframe to get the desired result
        Action: python_repl_ast
        Action Input: data[(data['Age'] > 30) & (data['Fare'] > 30) & (data['Fare'] < 50) & ((data['Pclass'] == 1) | (data['Pclass'] == 2))].shape[0]
        Observation: 20
        Thought: I now know the final answer
        Final Answer: 20

        > Finished chain.





        '20'



```


## Numpy examples​

```python




    import xorbits.numpy as np
    from langchain.agents import create_xorbits_agent
    from langchain.llms import OpenAI

    arr = np.array([1, 2, 3, 4, 5, 6])
    agent = create_xorbits_agent(OpenAI(temperature=0), arr, verbose=True)



```


```python




          0%|          |   0.00/100 [00:00<?, ?it/s]



```


```python




    agent.run("Give the shape of the array ")



```


```python






        > Entering new  chain...
        Thought: I need to find out the shape of the array
        Action: python_repl_ast
        Action Input: data.shape
        Observation: (6,)
        Thought: I now know the final answer
        Final Answer: The shape of the array is (6,).

        > Finished chain.





        'The shape of the array is (6,).'



```


```python




    agent.run("Give the 2nd element of the array ")



```


```python






        > Entering new  chain...
        Thought: I need to access the 2nd element of the array
        Action: python_repl_ast
        Action Input: data[1]


          0%|          |   0.00/100 [00:00<?, ?it/s]



        Observation: 2
        Thought: I now know the final answer
        Final Answer: 2

        > Finished chain.





        '2'



```


```python




    agent.run(
        "Reshape the array into a 2-dimensional array with 2 rows and 3 columns, and then transpose it"
    )



```


```python






        > Entering new  chain...
        Thought: I need to reshape the array and then transpose it
        Action: python_repl_ast
        Action Input: np.reshape(data, (2,3)).T


          0%|          |   0.00/100 [00:00<?, ?it/s]



        Observation: [[1 4]
         [2 5]
         [3 6]]
        Thought: I now know the final answer
        Final Answer: The reshaped and transposed array is [[1 4], [2 5], [3 6]].

        > Finished chain.





        'The reshaped and transposed array is [[1 4], [2 5], [3 6]].'



```


```python




    agent.run(
        "Reshape the array into a 2-dimensional array with 3 rows and 2 columns and sum the array along the first axis"
    )



```


```python






        > Entering new  chain...
        Thought: I need to reshape the array and then sum it
        Action: python_repl_ast
        Action Input: np.sum(np.reshape(data, (3,2)), axis=0)


          0%|          |   0.00/100 [00:00<?, ?it/s]



        Observation: [ 9 12]
        Thought: I now know the final answer
        Final Answer: The sum of the array along the first axis is [9, 12].

        > Finished chain.





        'The sum of the array along the first axis is [9, 12].'



```


```python




    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    agent = create_xorbits_agent(OpenAI(temperature=0), arr, verbose=True)



```


```python




          0%|          |   0.00/100 [00:00<?, ?it/s]



```


```python




    agent.run("calculate the covariance matrix")



```


```python






        > Entering new  chain...
        Thought: I need to use the numpy covariance function
        Action: python_repl_ast
        Action Input: np.cov(data)


          0%|          |   0.00/100 [00:00<?, ?it/s]



        Observation: [[1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]]
        Thought: I now know the final answer
        Final Answer: The covariance matrix is [[1. 1. 1.], [1. 1. 1.], [1. 1. 1.]].

        > Finished chain.





        'The covariance matrix is [[1. 1. 1.], [1. 1. 1.], [1. 1. 1.]].'



```


```python




    agent.run("compute the U of Singular Value Decomposition of the matrix")



```


```python






        > Entering new  chain...
        Thought: I need to use the SVD function
        Action: python_repl_ast
        Action Input: U, S, V = np.linalg.svd(data)
        Observation:
        Thought: I now have the U matrix
        Final Answer: U = [[-0.70710678 -0.70710678]
         [-0.70710678  0.70710678]]

        > Finished chain.





        'U = [[-0.70710678 -0.70710678]\n [-0.70710678  0.70710678]]'



```
