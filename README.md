
Modelio3WorkspaceGenOCL-G99
===========================

Summary
------------
This repository contains the necessary elements to build an OCL
generator from UML thanks to the Modelio Open Source tool.
It will allow you to create a basic modelio 'workspace' with some
example projects and a place to define the code of your generator
as a modelio 'macro'. Macros are written in jython, that is
a python engine running on a JVM.

Installation
---------------
1. Install modelio if not already done.

2. Download WorkspaceGen-OCL-99 as an archive. The best is to
   download it from GitHub as you will always get the last version.
   For this you can go to the [project on github](https://github.com/megaplanet/Modelio3WorkspaceGenOCL-G99)
   and use the 'download zip' button (the last button on the right
   pane). Github will create a zip of the project
   (with -master.zip at the end because this is the 'master'
   branch. You will remove this after)

2. Extract the **WorkspaceGenOCL-G99 ... .zip** archive in a
   place of your preference. This will create a directory with a
   name like WorkspaceGenOCL-G99 xxx .

3. **Rename this directory**: replace 99 by your group number
   and remove what might follow (e.g. -branch). You should
   now have on your disk a repository like WorkspaceGenOCL-G17
   if you have the group number 17. This directory will be used
   later as your modelio workspace.

4. Launch modelio. Modelio will start with a default 'workspace'
   create somewhere. We will not use it.

5. Select the your workspace as following:

   * Menu "File > Switch Workspace"

   * Select the directory WorkspaceGenOCL-Gxx that you've
       just renamed.

   * Modelio shows the workspace. You should see no projects
      (on the left panel). But three 'macros' should appear on the
      tool bar: "*Sandbox*", "*Generate OCL*" and "*CoExplorer*".
      The purpose of these macros will be explained later and you
      will be able to modify the first two ones.

6.  Import the UML projects that will be used to test your
      transformations. These projects are provided in the form
      of a 'project archives'. They are .zip files which is the
      standard way to exchange project in modelio.
      Follow the following procedure for each project (see below):

    * Menu "File > Import a project"

    * Select one of the .zip archives in the directory
       'WorkspaceGenOCL-Gxx/_PROJECT_ARCHIVES'

    * The project should now appear in the left panel.

    * Repeat this operations for all 'project archives' in the directory.

You are now ready to play.

Executing python code from the 'script' console
-----------------------------------------------
In this section you will learn how to use the script console of
Modelio. This is a really excellent feature of Modelio as this
allowed to play interactively with models, explore the metamodels,
experiment with transformations, etc.

1. Open the 'CyberResidence' project.

2. Using the browser on the left select some classes.

3. Menu 'View > Script'. This open the python engine (it takes a
     few second the first time).

4. type 'print "Hello World"' in the console and press Ctrl-Enter

5. You can observe the result...

6. Then copy-paste the following program to the console and press Ctrl-Enter

         for c in selectedElements:
            if isinstance(c,Class):
                attributes = c.ownedAttribute
                print '<h2> %s <\h2>' % c.name
                print 'The class %s has %i attributes: <ul>' % (c.name, len(attributes))
                for a in attributes:
                   print '<li> %s : %s </li>' % (a.name, a.type.name )
                print '</ul>'

7. You may get an error message like the following one (displayed in red)
     '... line 1 ... SyntaxError: mismatched input '  ' expecting EOF'.
    If so this is due to some extra spaces in the copy paste.
    Python is based on the indentation to represent block,
     so if there are some spaces before the first line (for c ...) the interpreter
     will complain: a top level statement is expected (hence no spaces).
     As you can see, the code  you have just pasted has disappeared
     when you press Ctrl Enter, not really convenient... Press the icon
     that looks like a 'blue gearing' (the penultimate logo in the console toolbar).
     The tooltip on this logo is 'Activate/Desactivate debug mode'. In fact,
     it just allows to keep the text in the console instead of erasing it when
     Ctrl-Enter is pressed. Copy the program above again, check for spaces
     and press enter again. Now the program stay in the console so if there
     are still some space problem you can correct the program there.

8. At some point you will get the following error:
     '... line 6 ... expecting COLON'
    This is because all composed statement (for ... : , if ... :,  etc) must
     have ':' at the end to indicate that a new block is going to start.
     Java programmers often tend to forget this ':' and will get this error.
     Otherwise the python syntax is straight forward.
     Correct the program by adding ':' after 'for a in attributes' and
     press Ctrl-Enter. You know have a little html generator. If you
     select some classes in modelio browser and run the program
     you see the list of classes with their attribute in html.
     Obviously if you want to see a nice result you should put this in
     a .html file and launch a browser, but this is another story.


Executing python code as macros
------------------------------------
Writing code in the console provides a very convenient way to test
some small snippet of programs interactively. This is an excellent
advantage of the Modelio environment.

If you want however to develop a more complex program and deliver it
to other users, you have to use Modelio 'macros'. Macros are just
python program saved in a file. That's all. Macros can be located
in three difference places (but not elsewhere, this is a current
limitation of Modelio):

1. Project macros. This location is only useful for macro that are
   specific to a particular projects. Most of the time this is not
   the case. So the project location is seldom used.

2. Workspace macros. These macros can be used in all projects within
   this location. We are going to use this location as this is the
   most convenient one. In this tutorial the workspace is obviously
   the WorkspaceGenOCL-Gxx with your group number.

3. System macros. These macros are located in your .modelio directory,
   but are normally not for users-defined macros.

Macros are organized in 3 'macros catalogs' according to the location
above. If you are curious you can have a look to the menu
'Configuration > Macros Catalog...' but we are actually no going to
use this graphical interface. To save your time, the workspace provided
already comes with 3 macros already registered in the corresponding
catalog. What you need is just an your system file browser and
a textual editor (e.g. Notepad++ on windows) to edit the macros.

1. Open the directory WorkspaceGenOCL-Gxx with your file browser.
   There is a **macros** directory. Open it. It contains different
   files: .catalog, and some *.py files which are macros written
   in python.

2. The **.catalog** file list the registered macro, and indicates
   how they should be included in the modelio user interface and
   some additional information. If you are curious look at the
   content of the  .catalog file. We are not going to change it as
   the three macros in the directory are already referenced properly
   by this file. In fact, modelio macro interface mentioned above
   is just used to modify this file. One can edit it instead with
   a text editor. Again, you can leave this file as we will not use it.

3. The **Sandbox.py** is an extended 'Hello World' macros. You can
   execute this macro using "Sandbox" button in the modelio toolbar.
   (If you don't see this label in the toolbar you should restart
   modelio and make sure that you are using the WorkspaceGenOCL-Gxx
   workspace). To edit a macro you just have to edit the python file
   with your favourite editor. For instance Notepad++ is a good option
   on windows. It will highlight python keywords, etc.
   You can modify and do whatever you want with the sandbox.py. This
   is your playground. Just make some modifications, save the file
   and press the Sandbox button to see immediately the result.

4. The **GenOCL.py** is the macro that **will constitute the result of you
   work**. You will put there all the python code that allow to generate
   a USE OCL model from a class model. To be more precise, when
   a package is selected in the modelio browser, executing this macro
   will generate the corresponding USE OCL code. Currently the file contains
   only some hints to structure this transformation.

5. The **CoExplorer.py** is a tool written to simplify your life
   (at least the part related with modelio). This macro allows
   to explore at the same time the model and metamodel.
   This macro is not indented to be modified, unless you find bugs and
   correct them, or want to improve it. This macro is available from the
   [official 'Modelio Stone'](http://www.modeliosoft.com/en/modelio-store)
   It has been included directly in the WorkspaceGenOCL-Gxx
   workspace in order to save you time. If you find some bug or
   have some observations your can post a comment there. And if you find
   it useful you can rate it as well. To try it just select some
   arbitrary model element in modelio browser and press 'CoExplorer'
   in the toolbar.

Modelio projects in the workspace
---------------------------------------
Now that we have reviewed how to use the console and how macros work
just let us have a look at the modelio project delivered with modelio.

1. Open the CyberResidences project in modelio if not already done.
  This project contains the full CyberResidences model apart from the
  constraints. If you browse this project you should find at the third
  level (or forth depending on a display configuration) a package
  'CyberResidences' marked with a 'C' letter. This icon does not come
  from modelio but comes with the 'Constraint Profile' embedded in the
  model (more later). By selecting this package, the macro
  'GenerateOCL' should generate the corresponding USE OCL text. This
  is your work. You will have before to enter the different constraints.

2. Close this project and open the UMLTestCases project. Browse the
  content of this project. You will see that in the package ClassModels
  they are plenty of very small projects with increasing complexity,
  or that contains only a few UML constructs in isolation. For instance
  a model contains only Classes, some other only Classes and Attributes,
  some others only Inheritances, only Association Classes, etc. This
  project is intended to allow you to test you OCL generator in an
  incremental way. For instance you can first implement the generation
  of classes, then test the generator with the corresponding package.
  Then implement the generator for attributes and test it with a project
  with attributes, and so on. Your development could be driven by the
  list of features in UML and the provided test cases. This is some form
  of Test Driven Development (TDD) at work. Note that note all constructs
  are available in USE OCL: this set of test cases have been developed
  to test arbitrary transformation based on class diagrams, not
  specifically the class diagram to USE OCL transformation.

3. Close this project and open the project Sandbox. This project is
   empty. This is your playground. Use it if you want to play with
   modelio features or create your own models. Unless mentioned
   explicitly you are not expected to modify the other projects.

Time to work
------------
It now time to work. You job is to write the content of GenOCL macro
incrementally. You can follow any kind of process, but here are some
possible ideas.

1. **Split the work among members of the group**. You have first to discuss
   with your colleague on your groups and decide how to split the work.
   For instance you can define who is going to write which functions
   (see the content of GenOCL.py for some hints on the hint of the whole
   program). You can 'drive' these decisions by observing the structure
   of the UML metamodel. For instance writing generation for attributes
   is independent from writing generation for methods. Playing a bit
   with the actual metamodel of modelio, will show you that one will have
   to write methods to get association classes, etc. These different
   functions can be elaborated separately.

2. **Select a test case in UMLTestCases** that has been assigned to you.
   Open this project. Use CoExplorer to check how the model is structured
   according to modelio metamodel.

3. **Dealing with the source metamodel**. Here this is UML.
   Use the console to check which python expressions are required to get
   the relevant information from the UML model. If these expressions are
   not trivial  you might want to write a general purpose metamodel helpers
   (see GenOCL.py). After testing them interactively the best is to put it
   in GenOCL.py so that you can reuse it.

4. **Check how to deal with the target metamodel**. Here this is the USE
   OCL language. The metamodel is indeed the textual syntax available
   in the documentation. This step is necessary to see what is possible
   to translate exactly with USE OCL. You will see for instance that
   an association can have more than two roles...  This step also allow
   you to check which syntax you have to generate.

5. **Mapping the source metamodel to the target metamodel**.
   Once the functions for extracting the source metamodel (UML) are ok,
   and you know what to produce w.r.t target metamodel (USE OCL)
   you can write the function(s) that use the helpers defined before
   and produce the corresponding USE OCL text. Again you can start
   playing in the console and then when everything is fine add new
   functions to GenOCL.py.

5. **Synchronization points**. At some point you will have to synchronize
   with other groups members. For instance when some functions depend from
   functions written by someone else. Or simply because it is always good
   to synchronize to avoid divergence. That is, do not wait for the end for
   synchronizing your work and realize that many incompatible elements have
   been produced.

6. **Integration tests**. Use the CyberResidences project to test the
   generate as a whole.

That's all folk.
