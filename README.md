# JSON to HTML Converter test task
## Text of the task:
Imagine that you have a new empty project. The task of this project is to convert
JSON format in HTML.
Below is a sequence of customer requirements. Each requirement from a relative to the finished task, the result of which will be sent to the production. IIf there are more commits than tasks, then you need to make sure that a commit with a completely completed next task will be flagged. Tests for the entire code are not required.
Need to write only a couple of tests on functions. In total, 4 tasks. Each task was made on the basis of the previous one.
###Notes:
The program must read the file on the disk with the name **source.json** and print output to **stdout**
##Usage:
Consider the 4th task.
* Open source.json file.
```json
[
  {
    "span":"Title #1",
    "content":[
      {
        "p": "Example 1",
        "header": "header 1"
      }
    ]
  },
  {"div":"div 1"}
]

```
* Run a program. You receive a converted output in stdout.
```html
<ul><li><span>Title #1</span><content><ul><li><p>Example 1</p><header>header 1</header></li></ul></content></li><li><div>div 1</div></li></ul>
```
###Notes:
* According to the task, each element in the **list** (in "[]" brackets)should be placed in the tag **ul**
* Each element inside the list should be placed in the tag **li**
### Tests:
I used a simple unit test, that compares stdout of the program and expected result.
#### License
[MIT](https://choosealicense.com/licenses/mit/)