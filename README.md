# python_async_chat


## About packages

`client`
client application, can be used with any GUI application
###### import rules:
- imports from utils allowed
- imports from any other packages not allowed  

`server`
tcp server application, can be used with any client application
###### import rules:
- imports from utils allowed
- imports from any other packages not allowed

`utils`
package with utils functions and classes
###### import rules:
- imports from any other packages not allowed

`desktop`
GUI PyQt based application
###### import rules:
- imports from utils, client allowed
- imports from any other packages not allowed
