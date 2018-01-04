
# coding: utf-8

# # Largest Continuous Sum
# 
# ## Problem
# Given an array of integers (positive and negative) find the largest continuous sum. 
# 
# ## Solution
# 
# Fill out your solution below:

# In[1]:


def large_cont_sum(arr): 
    
    max_sum = cur_sum = arr[0]
    
    for num in arr[1:]:
        
        cur_sum = max(cur_sum + num, num)
        max_sum = max(cur_sum, max_sum)
    return max_sum


# In[2]:


large_cont_sum([1,2,-1,3,4,10,10,-10,-1])


# ____
# Many times in an interview setting the question also requires you to report back the start and end points of the sum. Keep this in mind and see if you can solve that problem, we'll see it in the mock interview section of the course!

# # Test Your Solution

# In[4]:


from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)


# ## Good Job!
