package com.ontio.testtool.utils;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Logger {
	private static Logger instance = null;
	private static FileWriter logfileWriter = null;
	private static File logfile = null;
	private static FileWriter collectionfileWriter = null;
	private static String logfilename = null;
	private static String logname = null;
	
	private static String collectionfileName = "collection.csv";
	private static String prefixpath = "";
	private static String subFolder = "";
	private static String casestate = "";
	private int step = 1;
	public static synchronized Logger getInstance(){
        if(instance == null) {
            instance = new Logger();
        } 
        return instance;
    }
	
	public Logger() {
		SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd_HH-mm-ss");
		//SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd");
		String date = df.format(new Date());
		
		prefixpath = "logs/" + date;  
		File file = new File(prefixpath);
		if(!file.exists()) {  
		    file.mkdirs();  
		}
	}
	
	public String getPrefixPath() {
		return prefixpath;
	}
	
	public void setType(String type) {
		subFolder = type;
		if (!subFolder.isEmpty()) {
			subFolder += "/";
		}
	}
	
	public File logfile() {
		return logfile;
	}
	
	public void print(String content) {
		try {
			write("[ INFO    ]  " + content);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	};
	public void error(String content) {
		try {
			write("[ ERROR   ]  " + content);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	};
	public void warning(String content) {
		try {
			write("[ WARNING ]  " + content);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	};
	public void description(String content) {
		try {
			write("[ DESCRIPTION ]  " + content);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	};
	public void step(String content) {
		try {
			write("[ STEP    ]-" + step + "  " + content);
			step++;
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	};
	
	public boolean open(String logfilename, String logname) {
		try {
			step = 1;
			logfile = new File(prefixpath + "/" + subFolder + logfilename);
			File fileParent = logfile.getParentFile();  
			if(!fileParent.exists()){  
			    fileParent.mkdirs();  
			}
			
			logfileWriter = new FileWriter(prefixpath + "/" + subFolder + logfilename);
			Logger.logfilename = logfilename;
			Logger.logname = logname;
			System.out.print("\n");
			System.out.print("\n");
			write("[---------------------" + logname + "--------------------]");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}
		return true;
	};
	
	public boolean appendRecord(String name, String status, File logfile) {
		String filePath = logfile.getParentFile().getAbsolutePath() + "/" + collectionfileName;
		
		try {
			if (collectionfileWriter == null) {
				File file = new File(filePath);

				if (!file.exists()) {
					collectionfileWriter = new FileWriter(filePath, true);
					collectionfileWriter.write("NAME,STATUS,LOG PATH\n");
				} else {
					collectionfileWriter = new FileWriter(filePath, true);
				}
				collectionfileWriter.write(name + "," + status + "," + logfile.getName() + "\n");
				collectionfileWriter.close();
				collectionfileWriter = null;
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}
		return true;
	}
	
	public boolean close(String ret, String info) {
		try {
			if (info == null) {
				info = "";
			}
			if (ret.toUpperCase().equals("PASS")) {
				write("\n\n[ Pass    ]    (" + info + ")");
				casestate = "pass";
			} else if (ret.toUpperCase().equals("FAIL")) {
				write("\n\n[ Fail    ]    (" + info + ")");
				casestate = "fail";
			} else {
				write("\n\n[ Block   ]    (" + info + ")");
				casestate = "block";
			}
			write("[---------------------   END   ---------------------]");
			
			appendRecord(logname ,ret, logfile);
			
			if (logfileWriter != null) {
				logfileWriter.close();
				logfileWriter = null;
			}
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			if (logfileWriter != null) {
				try {
					logfileWriter.close();
					logfileWriter = null;
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			}
			return false;
		}

		return true;
	};
	
	public String state() {
		return casestate;
	}
	
	public void setBlock() {
		try {
			if (logfileWriter != null) {
				logfileWriter.write("[ Block    ]");
			} else {
				FileWriter fw = new FileWriter(prefixpath + "/" + subFolder + logfilename, true);
				fw.write("[ Block    ]");
				fw.close();
			}

			appendRecord(logname ,"block", logfile);
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void write(String contents) throws IOException {
		SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
		String date = df.format(new Date());
		
		String[] splitstr = contents.split("\n");
		
		contents = "";
		for(int i = 0; i < splitstr.length; i++) {
			String splitstrele = splitstr[i];
			contents = date + ": " + splitstrele + "\n";
		}
		
		System.out.print(contents);
		if (logfileWriter != null) {
			logfileWriter.write(contents);
		}
	}
}
