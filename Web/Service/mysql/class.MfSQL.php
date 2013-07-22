<?php
 
include "mysql/class.MySQL.php";

class MF_SQL{

	var $mySql;

	var $username;
	var $password;
	var $database;
	var $host;

	var $username_key = 'username';
	var $password_key = 'password';
	var $database_key = 'database';
	var $host_key = 'host';

	/* *******************
	 * Class Constructor *
	 * *******************/

	function Mf_SQL(){
		// get database properties from ini file
		$this->loadDatabaseProp();
		// init the sql obj
		$this->mySql = new MySQL($this->database, $this->username, $this->password, $this->host);
	}

	public function getMySql(){
		return $this->mySql;
	}


	function loadDatabaseProp(){
		$config = parse_ini_file("db_config.ini");
		$this->username = $config[$this->username_key];
		$this->password = $config[$this->password_key];
		$this->database = $config[$this->database_key];
		$this->host = $config[$this->host_key];
	}	
}

?>