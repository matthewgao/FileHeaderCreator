# FileHeaderCreator
Create a header for each new file or empty file.

##Example

###For C/C++ header file
~~~
/*
 * an.h
 * Created By: Matthew Gao
 * Copyright (c) Dell.Inc
 * Created Time: 2015-10-07
 */
#ifndef _AN_H
#define _AN_H


#endif
~~~

###For C/C++ cpp file
~~~
/*
 * an.cpp
 * Created By: Matthew Gao
 * Copyright (c) Dell.Inc
 * Created Time: 2015-10-07
 */
~~~

###For Python3 file

~~~
#!/usr/bin/env python3
# coding=utf-8
# Created Time: 2015-10-07

__author__ = 'Matthew Gao'
~~~

##Configuration
Add two configurations in `Preference->Settings->User`

~~~
{
    "author1" : "Matthew Gao",
    "company" : "Copyright (c) Dell.Inc"
}
~~~