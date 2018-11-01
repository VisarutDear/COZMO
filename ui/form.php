<?php  
 $message = '';  
 $error = '';  
 if(isset($_POST["submit"]))  
 {  
      if(empty($_POST["name"]) or empty($_POST["med"]) or (empty($_POST["hour"] and $_POST["minute"])) or empty($_POST["quantity"]))  
      {  
           $error = "<div class='alert alert-danger'><strong>Incomplete Values!</strong> There is an incomplete fields in your submission</div>";
      }   
      else  
      {  
           if(file_exists('data.json'))  
           {  
                $current_data = file_get_contents('data.json');  
                $array_data = json_decode($current_data, true);  
                $extra = array(  
                     'name'         =>     $_POST["name"],  
                     'med'          =>     $_POST["med"],  
                     'hour'         =>     $_POST["hour"],
                     'minute'       =>     $_POST["minute"],
                     'quantity'     =>     $_POST["quantity"],
                     'relative'     =>     $_POST["relative"],
                     'line'         =>     $_POST["line"]     
                );  
                $array_data[] = $extra;  
                $final_data = json_encode($array_data);  
                if(file_put_contents('data.json', $final_data))  
                {  
                     $message = "<br><p class='text-success pull-right' style='font-size: 11px'><b>Your data has been successfully saved</b></p>";  
                }  
           }  
           else  
           {  
                $error = 'JSON File not exits';  
           }  
      }  
 }  
 ?>  
 <!DOCTYPE html>  
 <html>  
    <head>  
        <title>Prescription</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        
        <style>
        body{
          background-color: #f6c129;
          font-family: sans-serif;
        }
        .container{
          width: 38%; height: 90%;
          background-color: #FFF;
          margin-top: 30px; margin-bottom: 30px;
          padding: 20px 30px 20px 30px;
          border-radius: 2px;
          border-radius: 2px;
          box-shadow: 0px 2px 7px rgba(0.3, 0.3, 0.3, 0.3);	
          position: relative;
        }
        h1{
          font-size: 28px;
          font-weight: 500;
          color: #6753d8;   
        }
        p{
          font-size: 15px;
          line-height: 7px;
          color: #a6a3a7;   
        }
        h5.hpurple{color: #6753d8;}
        .form-group.required .control-label:after{
          content:" (required)"; color:red;
        }
        ul.dob li{
          display:inline-block;
          margin-bottom: -15px;
          margin-right: 30px; 
        }
        ul.dob li:not(:last-child){margin-right:20px;}
        input[type=submit]{background-color: #6753d8; width: 20%}
        input[type=submit]:hover{background-color: #5b49c5; width: 20%}

        #foot{
          margin-top: 10px;
          color: #a6a3a7;
          font-size: 14px;
        }
        #foot:hover{text-decoration: underline;}
        </style>

    </head>  
    <body>  
    <div class="container">
        <h1 class="text-center">YOUR PRESCRIPTION</h1>
        <p class="text-center">Please complete all information requested on this form</p>
            
            <br><h5 class="hpurple">Medical Information:</h5>
            <form method="post">  
                <?php   
                if(isset($error))  
                {  
                    echo $error;  
                }  
                ?>  
                
                <div class="form-group required">
                    <label class="control-label">What's your name?</label>
                    <input type="text" name="name" class="form-control" placeholder="e.g., Jane Doe">
                </div>     
                <div class="form-group required">
                    <label class="control-label">What's your medicine name?</label>
                    <input type="text" name="med" class="form-control" placeholder="e.g., Paracetamol">
                </div>

                <div class="form-group required">
                  <label class="control-label">When do you need to take it? </label>
                    <center><ul class=dob>
                      <li><div class="form-group">
                        <label>Hour:</label>
                        <select name="hour" class="form-control" id="sel1" style="width:100px">
                          <option>00</option><option>01</option><option>02</option><option>03</option><option>04</option><option>05</option>
                          <option>06</option><option>07</option><option>08</option><option>09</option><option>10</option><option>11</option>
                          <option>12</option><option>13</option><option>14</option><option>15</option><option>16</option><option>17</option>
                          <option>18</option><option>19</option><option>20</option><option>21</option><option>22</option><option>23</option>
                        </select>
                      </div></li>
                      <li><div class="form-group">
                        <label>Min:</label>
                        <select name="minute" class="form-control" id="sel1" style="width:100px">
                          <option>00</option><option>05</option><option>10</option>
                          <option>15</option><option>20</option><option>25</option>
                          <option>30</option><option>35</option><option>40</option>
                          <option>45</option><option>50</option><option>55</option> 
                          </select>
                      </div></li>
                    <li><input id="btn2" class="btn btn-secondary btn-sm" type="button" value="+"></li>
                    </ul></center>
                </div>

                <div class="form-group required">
                  <label class="control-label">Number of medicine(s) which you need to take</label>
                  <select name="quantity" class="form-control" id="sel1">
                    <option>1/2</option>
                    <option>1</option>
                    <option>1.5</option>
                    <option>2</option>
                    <option>2.5</option>
                    <option>3</option>                  
                  </select>
                </div>
        
                <h5 class="hpurple">Your Relative's Information:</h5>
                <div class="form-group">
                  <label class="control-label">What's your relative name?</label>
                  <input type="text" name="relative" class="form-control" placeholder="e.g., John Doe">
                </div>
        
                <div class="form-group">
                  <label class="control-label">What's your relative contact's?</label>
                  <input type="text" name="line" class="form-control" placeholder="e.g., Line ID">
                </div>                    
			  			 
	
			   	      <br><input type="submit" name="submit" value="Submit" class="btn btn-primary pull-right"><br>     
				        <?php  
                     if(isset($message))  
                     {  
                          echo $message;  
                     }  
                     ?> 
                     
		
		<br><a onclick="window.open(this.href,this.target);return false;" href="http://127.0.0.1:5000/" target="whatever">
				        <p id="foot" class="pull-right">Show QRCode</p>   
						    </a>
                
              </form>  
           </div>  
      </body>  
 </html>  
