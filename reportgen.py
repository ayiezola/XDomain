htm1="""
<html>

<style>
/* = body
------------------------*/
body{
  background:#1abc9c;
}
.description{
  font-family: 'Vollkorn', serif;
  text-align:center;
  color:#ecf0f1;
  text-shadow:0 0.1em 0.2em #008c8d;
}
/* = Scroll body
------------------------*/
::-webkit-scrollbar{
  width:0.2em;
}
::-webkit-scrollbar-track{
  background-color:#bdc3c7;
}
::-webkit-scrollbar-thumb{
  background-color:#7f8c8d;
}
/* = table
------------------------*/
.box-table table{
  border-collapse:collapse;
  text-align:left;
  width:100%;
  margin:0;
  padding:0;
  background:#7f8c8d;
  animation: responsive 5s infinite ease-in-out;
}
.box-table{
  font:normal 12px/150% Arial, Helvetica, sans-serif;
  overflow:hidden;
  margin:0 auto;
  display:block;
  width:95%;
  padding:2.5%;
}
.box-table table thead th{
  background-color:#7f8c8d;
  color:#bdc3c7;
  text-align:center;
  padding: 0.75em;
  font-family: 'Vollkorn', serif;
  font-weight: bold;
  font-size: 1.5em;
  height: 1.5em;
  vertical-align: top;
  border-left:0.25em double #95a5a6;

}
.box-table table tbody td,
.box-table table tbody tr{
  font-family: 'Vollkorn', serif;
  font-size:1em;
  border:none;
  padding:1em;
}
.box-table table tbody tr:nth-child(odd){
  background:#ecf0f1;
  color:#95a5a6;
}
.box-table table tbody tr:nth-child(even){
  background:#bdc3c7;
  color:#7f8c8d;
}
.box-table table tbody tr a{
  text-decoration:none;
  color:#e67e22;
}
.box-table table tbody tr a:hover{
  color:#d35400;
}
.box-table .user-photo{
  background:#bdc3c7;
}
.box-table .user-tumb{
  width:6em;
  height:6em;
  padding:0;
  display:table-cell;
  text-align:center;
  margin:0 auto;
  -webkit-border-radius:100%;
  -moz-border-radius:100%;
  border-radius:3%;
}


/* = Responsive table
------------------------*/

/* http://elvery.net/demo/responsive-tables/  */
@media only screen and (max-width: 800px){
  .box-table table{
    width:100%;
    border-collapse:collapse;
    border-spacing:0;
  }
  .box-table th,
  .box-table td{
    margin:0;
    vertical-align:top;
  }
  .box-table th{
    text-align:left;
  }
  .box-table table{
    display:block;
    position:relative;
    width:100%;
  }
  .box-table thead{
    display:block;
    float:left;
  }
  .box-table tbody{
    display:block;
    width:auto;
    position:relative;
    overflow-x:auto;
    white-space:nowrap;
  }
  .box-table thead tr{
    display:block;
  }
  .box-table th{
    display:block;
    text-align:right;
  }
  .box-table tbody tr{
    display:inline-block;
    vertical-align:top;
  }
  .box-table td{
    display:block;
    min-height:1.25em;
    text-align:left;
  }
  .box-table th{
    border-bottom:0;
    border-left:0;
  }
  .box-table td{
    border-left:0;
    border-right:0;
    border-bottom:0;
  }
}
/* = Error
------------------------*/
.error_table {
  display: block;
  background: #E05E5E;
  color: #D1D1D1;
  font-family: 'Vollkorn', serif;
  text-align: center;
  font-size: 3em;
  width: 90%;
  padding: 5%;
}
/* = Loader
------------------------*/
.loading_table{
  background:#d35400;
  color:#ecf0f1;
  font-family: 'Vollkorn', serif;
  text-align: center;
  font-size: 1em;
  width: 0;
  display: block;
  overflow: hidden;
  height: 1em;
  padding:0.5em;
  animation: table_loader 10s infinite ease;
}
@keyframes table_loader{50%{width:100%}}
@-webkit-keyframes table_loader{50%{width:100%}}
@-moz-keyframes table_loader{50%{width:100%}}
@-ms-keyframes table_loader{50%{width:100%}}
@-o-keyframes table_loader{ 50%{width:100%}}

table img:hover { 
transition: transform .2s;
transform: scale(2.5);}
</style>

<body>

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>

<!-- Google fonts -->
<link href='https://fonts.googleapis.com/css?family=Vollkorn:400,700' rel='stylesheet' type='text/css'>

<!-- Description -->
<h1 class="description">
  XDomain Report from <a href="https://wikihak.com">wikihak.com</a>
</h1>

<!-- Table demo -->
<div class="box-table">
<table data-fn="contacts"></table>    
</div>


<script>

(function(){
  
  'use-strict';
  
  var elem,
      // data-fn
      dataFn = $('[data-fn="contacts"]'),
      // data-url
      thisUrl = dataFn.data('url');
  
  
    
    $.table_of_contacts = {};
  
  $.table_of_contacts.get = {
    
    init: function() {
      if(dataFn){
        this.getJson();
      }else{
        dataFn.html('No data found.');
      }
    },
    
    /* = Get data
    ------------------------*/
    getJson: function(url){
      
      var self = this;
      
      // loading data before
      dataFn.html('<span class="loading_table">'+
                  'Loading Please Wait ....'+
                  '</span>');
      
      // No ajax cache
      $.ajaxSetup({ cache: false });
      
      // Get json
      $.getJSON(thisUrl,function(data){
        
        // load template
        var out_html = self.tpl(); 
        
        $.each(data,function(i,obj){  
          // load inner template
          out_html += self.tpl_inner(obj);
          
        });
        // close tag
        out_html += '</tbody>';
        // render templates
        alert(out_html)
        dataFn.html(out_html);
        // error 
      }).error(function(j,t,e){ 
        // render error.
        dataFn.html('<thead><tr><th>Screenshot</th><th>Domain</th><th>Technologies</th><th>Open Ports</th><th>Coming soon!</th><th>Coming soon!</th></tr></thead><tbody>"""



htm2="""</tr></tbody>');
        
      });
    },
    

    
  };
  
  // on ready render data
  $(document).ready(function() {
    $.table_of_contacts.get.init();
  });
})().call(this);


</script>"""

def gen_html1(domain):
    with open(domain+'.html','w') as f:
        f.write(htm1)
        
def gen_html2(domain,x):
    with open(domain+'.html','a') as f:
        f.write('<tr><td class="user-photo"><img class="user-tumb" src="'+x[0]+'"></td>')
        f.write('<td><a href="'+x[1]+'" target="_blank">'+x[1]+'</a><br><a href="http://'+x[2]+'" target="_blank">'+x[2]+'</a></td>')
        f.write('<td>'+x[3]+'</td>')
        f.write('<td>'+x[4]+'</td>')

def gen_html3(domain):
    with open(domain+'.html','a') as f:
        f.write(htm2)
if __name__ == "__main__":
    main()