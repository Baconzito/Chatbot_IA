CREATE PROCEDURE [dbo].[sp_Get_User]
@Email nvarchar(50)

AS
BEGIN
	select * from Users where Email=@Email
END
GO
