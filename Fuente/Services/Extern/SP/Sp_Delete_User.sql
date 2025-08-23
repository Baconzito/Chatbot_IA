
CREATE PROCEDURE [dbo].[sp_Delete_User]
@Id int
AS
BEGIN
	update Users set Active=0 where Id=@Id
END
GO
