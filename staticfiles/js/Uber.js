// NavBar ABout Toggle
document.addEventListener('DOMContentLoaded',()=> {
    const DropCon = document.querySelectorAll('.Drop');
    DropCon.forEach(AboutCon => {
      const Rotate = AboutCon.querySelector('span');
      const About = AboutCon.querySelector('a');
      const DropMenu = AboutCon.querySelector('.DropMenu');
  
      About.addEventListener('click',()=> {
        Rotate.classList.toggle('Rotate');
        DropMenu.classList.toggle('DropOPen');
      });
  
      window.addEventListener('click',function(event){
        
        if(!event.target.matches('.Drop a')){
          DropCon.forEach(NewAbout => {
            const DropMenus = NewAbout.querySelector('.DropMenu');
            Rotate.classList.remove('Rotate');
            DropMenu.classList.remove('DropOPen');
          })
        }
      });
    });
    const UserMenu = document.querySelector('.UserToggle');
    UserMenu.addEventListener('click',()=> {
      UserMenu.classList.toggle('UserMenu');      
    }); 

    
  });


// Navbar 1100px NavToggle 
  let NavToggle = document.querySelector('.NavToggle');
    let NavMenu = document.querySelector('.NavMenu');
    let Main = document.querySelector('main');

    NavToggle.addEventListener('click',()=> {
      NavMenu.classList.toggle('NavMenuOpen');
      Main.classList.toggle('ViewPort');
      NavToggle.classList.toggle('NavOpen')

    });
  
// Checking User Logged Or Not

const UserHere = document.getElementById('UserHere');
const NotUser = document.getElementById('NotUser');
const Span = document.querySelector('.UserTextCon');
const value = Span.textContent;
if(value.length > 2){
    UserHere.style.display = 'flex';
    NotUser.style.display = 'none';

}else{
    NotUser.style.display = 'flex';
    UserHere.style.display = 'none';

};

// Active Toggle for Profile



// Construction Page For Unbuild Pages


