CREATE PROCEDURE [dbo].[sp_Get_User]
@Id int

AS
BEGIN
	select * from Users where Id=@Id
END
GO