# Hadoop and MapReduce

This is the final project for the [Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617) course from Udacity.  In this project we work with discussion forum (also sometimes called discussion board) data which is a type of user generated content that can be found all around the web.

##### Dataset and Virtual Machine

This particular dataset was taken from the Udacity forums the first months after the launch of this course.  Udacity forums were run on a free, opensource software called OSQA, which was designed to be similar to the popular StackOverflow forums. The basic structure is - the forum has nodes.  All nodes have a "body" and "author_id".  Top level nodes are called questions, and will also have a title and tags.  Questions can have answers.  Both questions and answers can have comments.

The MapReduce jobs were run on a VM.  The entire dataset "forum_data.tar.gz" and the instructions for setting up the VM can be found on the course [wiki page](https://www.udacity.com/wiki/ud617).  There are 2 files in the dataset. The first is "forum_nodes.tsv", which is the one used for the final project questions.  The most relevant field names to the final project questions are:

>"id": id of the node

>"title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty

>"tagnames": space separated list of tags

>"author_id": id of the author

>"body": content of the post

>"node_type": type of the node, either "question", "answer" or "comment"

>"parent_id": node under which the post is located, will be empty for "questions"

>"abs_parent_id": top node where the post is located

>"added_at": date added

##### Testing

Because of the large size of the original "forum_nodes.tsv" file, there is a sample file in this repository "student_test_posts.csv" with a portion of the nodes.  It can be used without the VM for testing the final project mapreduce code from the command line.  To test any mapreduce code from the command line you will need to use the following command:

`cat student_test_posts.csv | python <mapper file> | sort | python <reducer file>`   



## Questions

##### Students and Posting Time on Forums

Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.  Find for each student what is the hour during which the student has posted the most posts. Output from reducers should be: "author_id \t hour".  If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines. The order in which these lines appear in your output does not matter.

##### Post Length and Answer Length on Forums

We are interested to see if there is a correlation between the length of a post and the length of answers.  Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post.

##### Top 10 Question Tags

We are interested seeing what are the top tags used in posts.  Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

##### Potential Student Study Groups

We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.  As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
