CREATE PROCEDURE [dbo].[sp_Save_User]
@Id int=0,
@Email nvarchar(50),
@Password nvarchar(50)

AS
BEGIN
	if(@Id=0)
		insert into Users(Email,Password,Active) values(@Email,@Password,1)
	else
		update Users set Email=@Email, Password=@Password where Id=@Id
END
GO
